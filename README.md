# java-project-template
A basic template for a Bazel-powered Java project, linking in a few common libraries.

####Usage

You can try it out by cloning the repo and running all the tests. This will cause all depedencies to be fetched and all code to be built.

```
> bazel test src/...
```

In order to generate an eclipse project, run:

```
> src/tools/generate-eclipse-neon.py
```

Then, use `File > Import > General > Existing Projects into Workspace` to import the generated project into Eclipse. Whenever the project gets outdated (e.g., when a new library was added), the command above needs to be re-run.

####Requirements

* The `bazel` binary must be available on your path.
* You must have Python installed.

####Features

* An example library and binary, including tests.
* A third_party setup for external libraries.
* Support for grouping multiple Maven artifacts as a library.
* Support for generating an Eclipse project.

####Libraries

The default setup declares dependencies on:
* Guava
* JUnit
