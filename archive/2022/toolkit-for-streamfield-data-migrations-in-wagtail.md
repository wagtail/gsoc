# [Toolkit for StreamField data migrations in Wagtail](https://github.com/wagtail/wagtail-streamfield-migration-toolkit/discussions/17)

A brief summary of the work done for the GSoC 2022 Project - Toolkit for StreamField data migrations in Wagtail.
Refer the project files at https://github.com/sandilsranasinghe/wagtail-streamfield-migration-toolkit for the code and documentation.

#### The problem being solved

A streamfield is stored as a single column of JSON data in the database, where there are blocks stored (which can be nested to form complex block structures) within the JSON representation. However, as far as django is concerned when making schema migrations, everything inside this column is just a string of JSON data and the schema doesn’t change regardless of the content/structure of the StreamField since it is the same field type before and after the change. Therefore whenever changes are made to StreamFields, any existing data must be changed into the required structure by using a data migration created manually by the user.

Thus, a major problem developers using StreamField come across is writing data migrations when making changes involving blocks in the StreamField. While it is fairly straightforward for a very simple change like renaming a top level `CharBlock` it can easily become very complicated when nested blocks and multiple blocks are involved.

#### What the package provides

This package aims to make it easier for developers using StreamField who need to write data migrations when making changes involving blocks/block structure in the StreamField. We expose a custom migration operation class (MigrateStreamData) for migrations, which recurses through a streamfield to apply chosen sub-operations to all blocks matching a specific type. With it we also supply a set of sub-operations to perform the most common changes, while also allowing you to write your own when needed. In addition to updating the instance data, it also allows you to update revision data.

To go into more detail about what the package does, we could take a look at how writing a manual data migration would look like and what the package provides for it:

First, we would need to get the model from the current project state and query all the instances, do something to alter the data for each instance as needed, and then save it again. A similar process would be needed if revisions are being updated too. For this, the package provides a `MigrateStreamData` class which handles all the querying, applying changes and saving.

Secondly, for each instance, as mentioned earlier, once we have the data we need to alter the data as needed. Unlike in other fields where we directly have the specific data we need on the field directly, streamfields will contain other unrelated blocks, parent blocks etc. So we would have to recurse through different types of Streamfield structure (nested blocks in `StructBlock`, `StreamBlock`, `ListBlock`) and obtain the specific blocks which contain the data that we want to alter and map all the old blocks to new blocks. For this, the package provides functions for recursing through the different kinds of structures and obtaining blocks corresponding to a given block path. This process will also be called from within the above mentioned `MigrateStreamData` when the relevant block path/s are given.

Thirdly, once we get the blocks that we want to alter, we would need to write the logic for doing the actual change (for example renaming a block). For this, while we can't cover all possible changes, the package provides a set of sub 'operations' which cover common use cases like renaming blocks, removing blocks, moving a `StreamBlock` child inside a `StructBlock`, altering a value etc. It is possible to define custom sub operations for any other use cases. Again, using these sub operations is as simple as passing the required sub operation with parameters and the corresponding block path mentioned above to the `MigrateStreamData` class.

In addition to this functionality, the package aims to provide some tools to make it easier to generate data migration files without writing them manually. These would include a management command to generate a migration file including a given set of sub operations and blocks, and a management command which would be able to automatically detect any basic changes made after the last project state in the migration files.

#### Progress

Before the coding period started, the first step towards preparing for the project involved finding out what common changes were made by the community which required writing data migrations. Common use cases involved renaming and removing blocks, as well as moving a block inside a new `StructBlock`.

Work on the project started with an exploratory phase, creating some sample streamfields in a wagtail project and writing manual data migrations for changes made to it like renaming blocks, moving blocks inside structblocks etc. and updating corresponding revisions too. Here we addressed some questions about how to proceed, like how exactly we were going to access the streamdata, problems with validation when they were loaded into python objects, whether we were going to use block definitions to make sure we were accessing valid block paths etc.

Writing the actual code started with a somewhat test driven approach for creating the logic for recursing through types of streamfield structures. This involved writing tests with expected changes for raw (JSON like) data forming different structures with basic rename and remove operations. Following this the recursion logic as well as the data operations (rename, remove) were developed. One challenge here was to make sure we had a similar approach for structural operations like renaming blocks or moving them inside a new `StructBlock`, and for other operations like altering the value of a block.

By this point we had the functionality required to make the changes to the raw data. Next was querying the actual models and obtaining the required instance data, updating it with the operations and recursion utilities we developed and saving it. Here we had some problems related to working with the representation of models in the `ProjectState` at the time of the migration, which sometimes didn't contain all the methods and properties on the actual model. Since we had a considerable amount of migration related logic and this part was going to be called from the migration, we decided to make this a subclass of django's `migrations.RunPython`. Other things we had to consider here were optimizations when it came to iterating through a large queryset (for which we used a `queryset.iterator()` combined with a buffer and `bulk_update()`), as well as getting all the required revisions in a single query.

Next some time was spent on writing good descriptions/comments/docstrings for some of the more complex parts. In addition we started off with some basic documentation including references and some basic usage explanations. In addition, the testcases were refactored using the new version of wagtail factories (the previous version had limitations when it came to nested blocks which we needed a lot for the testcases). We were able to make the code for setting up data for our test cases a lot more compact and easier to read with it. We also worked on other data operations like alter value, combine blocks into a list block, move a block inside a new corresponding structblock etc. during this time.

Then we worked on writing testcases for the overall process of applying migrations (basically for the `MigrateStreamData` class). Here I had to learn about django's `ProjectState` and migration loaders a little, since we needed them to do the testing.

Before moving further, we had to address a couple of things which could cause issues. These included the change in the format used to save `ListBlock` data, since it was possible to have old data, especially in old revisions which was in this format whereas the rest of the data was in the new format if the project had upgraded wagtail. We also had to address what happened if a block path was given with matching data, but the block definition in the `ProjectState` did not include such a block. For this we wrote a custom exception and included raising it for instances and live/latest revisions and logging it otherwise.

So far we had written our code for wagtail 4. Now we started with adding support for wagtail 3, which had significant differences from wagtail 4 when it came to revisions, with the former having a `PageRevision` model with revisions available only for pages and the latter having changed it to a `Revision` model with revisions available for any model with the relevant mixins. We had some challenges here; having test cases some of which were not compatible for the different versions, querying the latest revisions for wagtail 3 (this was on account of the page models not having a latest revision property on them), and reusing code between the versions. After creating a separate test app for wagtail 4+ specific tests, writing a somewhat complicated query for the latest revisions and creating separate query maker classes for the different versions so that the rest of the code was common for the two versions, we were done here.

We also added a few more explanations to the usage guide in our documentation and generated the reference parts from the docstrings.

Next we started work on a command for generating migration files for a given operation and set of block paths. This would make it easier to generate a migration file as opposed to importing our utilities and writing it manually. It could be particularly handy in instances where the same kind of block is used in multiple StreamFields and it is renamed for example. Here, I had to see how django's `MigrationWriter` worked and use it for generating the required files.

At the same time we also started work on autodetecting changes made to streamfields (For now this was going to be limited to renames and removes). For this we compared the current `ProjectState` with the last `ProjectState` from the migration files to obtain the changes made to StreamFields. For this we had to look at how django's migrations, autodetecting etc. worked. Our approach included first obtaining all the autodetected changes to fields which django found and then filtering out the `AlterField` operations on `StreamField`s from which we obtained the previous and current `StreamField` definitions which we used in our own logic for detecting changes. Once we had the top level `StreamBlock` definitions, we recursively kept comparing their children and mapping old children to new children and hence finding rename and remove operations. For now the comparison logic assumes blocks with the same names are the same, and compares blocks which aren't mapped using comparer classes which give 'similarity scores' for different types of blocks (eg: StreamBlocks, StructBlocks), and asks the user whether a rename has occured for blocks which are above a certain similarity threshold, or if there are no blocks left to map whether a remove has occured.

#### Learning

The project was a great learning opportunity for me. I learnt a lot in the way of writing better and more reusable code, coding conventions in python as well as writing good comments/descriptions/docstrings, the last of which was something I barely used to do before. In addition I learnt a lot about wagtail, as well as how django's migration process works. A special thanks goes to the mentors Jacob (@jacobtoppm), Josh (@jams2) and Karl (@kaedroho) for their wonderful guidance and extensive code reviews.

#### PRs

- #3 , #5 : test cases for changes to the raw data
- #6 : functions for recursing through various streamdata structures and applying changes, test cases for more complex (nested) block structures, 'operations' for renaming and removing blocks
- #7 : `MigrateStreamData` class for applying the changes in a migration (subclass of django's `migrations.RunPython`
- #9 : more 'operations' and descriptions/better docstrings, refactoring test cases and using wagtail factories for all test data
- #11 : tests for applying migrations using `MigrateStreamData`
- #13 : support to handle data which may be in the old format (wagtail<2.15) used to store ListBlocks
- #16 : exception when the block def corresponding to the block path doesn't exist in the project state
- #8 : documentation
- #15 : wagtail 3 support
- #12 : a function for generating a migration file given an operation/s (eg: rename a block)
- #14 : basic autodetect; automatically detect basic changes (rename and remove blocks) made to streamfields and generate data migrations

#### What remains to be done

- improving autodetect process (better comparison and recognition of changes)

(Not in project goals, to be done in future)

- autodetect for more changes than basic renames and removes
- optimizing by making the changes in the JSONFields in the database where possible
- adding more intrafield operations for usecases needed by the community
- adding support for moving comments when their path changes due to streamfield changes
