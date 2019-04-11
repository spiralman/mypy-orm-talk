# Intro #

## Why are ORMs bad? ##

Coupling DB to Application, statefulness, lack of transparency

## Why are ORMs good? ##

Abstraction from DB, higher level DB access, reuse of common patterns,
schema enforcement

## What alternatives are there? ##

functional composition, built in data structures, bare classes

## What is MyPy? ##

It has nothing to do with databases. It's a static type checker.

Show:

* How to run it
* basic type checking: parameters and return values

Limitations:

* Can't check exceptions or side effects
* Can't tell you if what you do is *right*
    * You still need unit tests

# Building a Web App #

## Input Validation ##

Show:

* Describe data record (NamedTuple? TypedDict?)
* Construct data record from JSON
    * Fail if anything is missing

Record is `Book` with `title` and `author`.

## Write to Database ##

Show:

* Input data will always have required fields
* Refactor to add a new attribute in the DB
    * Type checking fails. must add attribute to data record
    * Validation function fails; must get data from input or fail

Refactor to add a required `publisher` attribute.

## Write Response ##

Show:

* Must handle writing errors.

# Optional Things #

## Update Data Record ##

Show:

* Add an optional attribute

Add optional `series` attribute

## Operate on Optional Attribute ##

Show:

* Add another type, without the attribute required
* Functions which need it take the type with the required attribute
* You must "guard" when converting from optional to required
* Once past the "guard", you are sure the attribute is there

Define `BookInSeries` that must have a series. Function like
`list_related` that finds the other books in the same series.

# Other Things? #

Some of these may be necessary for the above to make sense, but may
need to hand-wave or pre-write definitions, depending on time.

`BookWithId`? Need to distinguish between a `Book` that hasn't been
created yet (thus has no ID), versus one read from the DB (with an
ID).

Alternately, generating the ID as a GUID or ObjectID would solve
remove the need for that.

Talk about exceptions versus error return values and `Union[Book,
Error]`.

`NamedTuple` versus `TypedDict`: talk about whichever one doesn't get
used above.

Mention `async` and `await`?

`Any` for when you don't want type checking.
