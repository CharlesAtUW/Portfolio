"Huffman Exercise" | January 2024 | C++

---

This file compressor works by mapping more common bytes in the file to shorter bit sequences
(i.e., less than 8 bits). (This means that less common bytes might be mapped to a bit
sequence greater than 8 bits, but since they're less common, we overall get a smaller
compressed file size.)

The `HuffmanExercise` repository is available at
https://github.com/CharlesAtUW/HuffmanExercise/tree/efbbe937b6ebf7fa7ef82a05f29644410d9bf6ac
Its `README.md` contains essential information and documentation about the project,
including how to use the project.
The header (".h") files are also documented.

The `build` folder contains a binary executable build of the project. It was built in a
Linux environment. Directions for using it are in the `README.md` folder in the repository.