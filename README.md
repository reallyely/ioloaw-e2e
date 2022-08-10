# IOLAW Kinship Connector E2E Test

This repository holds a suite of automated tests that ensure the IOLAW Kinship Connector works as expected.
It can be used during development to shorten the development loop of `change --> test --> confirm` by making the tests consistent and lightning fast.

An End-to-End test is meant to follow a user's journey through an application and thereby test whatever subset of workflows desired. Full coverage is encouraged but we can start with the critical paths.

Given the [Layers of Testing](https://www.rainforestqa.com/blog/the-layers-of-testing-architecture), E2E tests the most things at once but is slowest. It should not be necessary to test some given functionality in each individual layer. If you've got it one, you're good to go. That means, if we have UI testing that flexes a given function, do we need to have a unit test for that function?  


## The Kinship Connector

Kinship Connector has two main components: A guided questionnaire to help **Applicants** fill out **Forms**

### Personas

- **Applicant** - the primary user that is expected to fill out the **Form**
- **Co-Applicant** - a secondary Applicant that could be identified on a **Form**
- **Recipient** - the recipient of the completed **Form**

### Entities

- **Form** - An Abstract Aggregate Entity with with the necessary information about a **Applicant**, 1-2 **Parents**, 1+ **Children**. Each subtype has different properties
  - **Guardianship**
  - **Adoption**
  - **Temporary Care**
- **Parent** - The parent of a **Child**. 
  - **Deceased** - A deceased parent
  - **Terminated** - A parent whose rights over the **Child** have been terminated
- **Child** - The subject the **Applicant** is applying for rights to 


## The Workflows

### As an Applicant I can select the form I know I need to apply for

#### Guardianship
#### Adoption
#### Temporary Care Agreement

### As an Applicant I can answer a questionnaire to determine what form I need

#### Guardianship
#### Adoption
#### Temporary Care Agreement

### As an Applicant I can apply for Guardianship