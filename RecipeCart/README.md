# RecipeCart"

- January-March 2023
- Java, MongoDB

---

The `CSE-403-RecipeCart` repository is available at
https://github.com/jteng2/CSE-403-RecipeCart/tree/8fbce444279f81095513f92ecea460ce28e31c41
The `README.md` file in the repository describes the project in more detail and
links to other very important documentation in the repository, such as
`user_manual.md`, `developer_manual.md`, `api_routes.md`, and the requirements
document.

The `recipecart-demo` folder contains an executable JAR of RecipeCart backend server,
along with a script to demonstrate its functionalities. There is also a video
of me going through this demo.

`Requirements.pdf` is a PDF copy of the requirements document linked in the
repository's `README.md`. It was a "living document" for our development process
of RecipeCart. It is long, so you don't have to read the whole thing, but the
main sections to look at are the "Use Cases (Functional Requirements)",
"Software Architecture", and "Software Design" sections. There were 5 use-cases
planned to be implemented during the project.

`Backend Architecture.pdf` is a PDF copy of the software architecture diagram
(mainly concerning the backend) in the requirements document.

`Backend Design.pdf` is a PDF copy of the `Design.pdf` in the "Software Design"
section of the requirements document. It is a UML-like class diagram, documenting
which classes have dependencies on which. Some things to note about it:
- Please refer to the key at the bottom-left of the diagram when reading it
 (I didn't know proper UML at the time of creating the diagram).
- "BLL" stands for "Business Logic Layer".
- `RequestTranslator` and `ResultTranslator` are now the classes named
 `RequestBodies` and `ResponseBodies` in the repository, respectively.

More things to note about this project:
- The frontend team did not get to implementing all 5 of the planned use-cases.
 So, when running the website, not all of the planned functionalities are
 doable through the website. But, all 5 of the planned use-cases were
 implemented on the backend (plus additional, smaller use-cases such as simply
 getting a recipe by its unique name).
- Neither the frontend team nor the backend (my) team got to fully addressing
 the non-functional requirements.
- In `user_manual.md`, the link to visit the website is no longer active (this
 was a class project). You will need to look at `developer_manual.md` for running
 the website and its backend server.
- `api_routes.md` documents, in detail, all of the outward-facing behaviors
 of the backend server (i.e., what HTTP requests to send it, and what it will
 send back), which includes the 5 planned use-cases.
- In particular, all files in the `src` folder, except for some in the
 `src/main/java/com/recipecart/database` folder, were coded by me.
- The class this project was for was Software Engineering, a (10-week) course
 where teams develop a project from the ground up, with much emphasis
 on the development process of the project.