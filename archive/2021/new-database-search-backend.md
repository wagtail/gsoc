# [New Database Search Backend](https://gist.github.com/ACMCMC/06b578b15b3b69f55f0c0127956afa12)

- Google Summer of Code 2021 project
- Student: Aldán Creo Mariño
- Mentors: Karl Hobley, Cynthia Kiser
- Organization: Django Software Foundation (in collaboration with Wagtail)

## Goal

The goal of my project is to replace the current default database search backend in Wagtail, which is a dummy backend that comes enabled by default, with a functional one that works on SQLite, PostgreSQL, and MySQL.

## Work that has been done

### Groundwork for the new Database Search Backend

In this part, I focused on refactoring the old `DatabaseSearchBackend` to be just a fallback backend that would get used when no other backend is available. The `DatabaseSearchBackend` just performs an `icontains` query. I moved it to be part of the new `wagtail.search.backends.database` module, as the `fallback` backend.

I also implemented a method in the `__init__` file, which is responsible for returning the most appropriate search backend. For example, if the current database is a PostgreSQL database, the PostgreSQL search backend gets returned. This allows the user to only specify `wagtail.search.backends.database` as their `WAGTAILSEARCH_BACKEND` in the config file, without having to choose a specific one (even though the ability to manually choose one remains intact).

For every backend, there was the need to implement, among others:

- A specific migration (`wagtail.search.migrations`) for the adequate table(s) in the DB to be created.
- A subclass of the `BaseSearchBackend` that adds behaviour specific to the database system being used.
- Utility files for use in the specific search backend.
- Tests for the backend.

I asked a question in the [Django Forums](https://forum.djangoproject.com/t/different-models-for-different-databases/8471) to get insigths for this part of the work.

This work has been submitted in the [#7281 wagtail/wagtail PR](https://github.com/wagtail/wagtail/pull/7281).

### PostgreSQL Search Backend

I worked into refactoring the existing `wagtail.contrib.postgres_search` app, into the new `wagtail.search` app, as a specific backend of the `wagtail.search.backends.database` structure. I kept the existing structure of the original database models that were created in the contrib module, and the references to Django PostgreSQL specific full-text fields.

This work has been submitted in the [#7305 wagtail/wagtail PR](https://github.com/wagtail/wagtail/pull/7305).

### SQLite Search Backend

For this backend, I implemented a 'shadow copy' model that enables to perform full-text searches in a table that mirrors a base table containing the `body`, `title` and `autocomplete` `TEXT` columns. The 'shadow table' is a virtual table using the SQLite FTS5 module. Documentation about SQLite full-text search capabilities can be found [here](https://www.sqlite.org/fts5.html).

I asked some questions on public forums on this part of the project:

- [Django Forums](https://forum.djangoproject.com/t/field-lookups-but-not-on-fields/9047).
- [Stack Overflow](https://stackoverflow.com/questions/68652308/unary-not-in-sqlite-fts5-match-query).
- [SQLite Forums](https://sqlite.org/forum/forumpost/9dafa0de932dda34bd561153a07bb3e18688633b7c13afffa5509b00a5ee2559).

This work has been submitted in the [#7420 wagtail/wagtail PR](https://github.com/wagtail/wagtail/pull/7420).

### MySQL Search Backend

The MySQL backend was the last part of the work done. This backend was implemented without the need for a shadow table. That's because MySQL directly supports defining `FULLTEXT` indexes on `TEXT` columns, as [the docs](https://dev.mysql.com/doc/refman/8.0/en/fulltext-search.html#function_match) specify. The search queries are performed in boolean mode.

I asked a question in [Stack Overflow](https://stackoverflow.com/questions/68835748/nested-not-inside-an-and-in-mysql-full-text-search-queries) to get help in this part of the project.

This work has been submitted in the [#7445 wagtail/wagtail PR](https://github.com/wagtail/wagtail/pull/7445).

## Work left to do

- Support for autocomplete queries in the SQLite and MySQL backends.
- Ensure correct ranking of the search results in the SQLite backend.
- Support boosting in the SQLite and MySQL backends.
- Enable support for score annotations in the SQLite backend (should be easy work).
