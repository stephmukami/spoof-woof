
<h1 align="center">
  Image Hash Spoofing
  <br>
</h1>

<h4 align="center">A solution for image hash spoofing.</h4>
<p align="center">
  <a href="#background-ideation">Background and Ideation</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#limitations">Limitations</a> •
  <a href="#tech-skills">Technical Skills Gained</a> •
  <a href="#license">License</a>
</p>
<div align="center">
  
  <img src="https://media.giphy.com/media/mGLOwWFI72JQvxsYaS/giphy.gif?cid=ecf05e47hiuuxng4pbn3yyelv8kho5x7avvq6ytx3bq38yj1&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="gif page" width="150" height="150">
  
</div>

## Background and Ideation
### **Solution Overview**

This solution is inspired by the [**Birthday Problem**](https://en.wikipedia.org/wiki/Birthday_problem), a probability puzzle that demonstrates how the likelihood of a collision increases counterintuitively with more data points. The goal of this solution is to process an image into a hash and find a collision where two different inputs produce the same hash, such that the resulting image remains visually unchanged when the hash is reversed.

#### **Approach**
1. **Hash Collision**: The program aims to modify the hash such that it matches the desired prefix with minimal visual changes to the image. This is achieved by altering non-visible components like:
   - **EXIF Data**: Metadata changes that don't affect the image visually.
   - **Least Significant Bits (LSBs)**: Slight pixel alterations that are imperceptible.
   - **Compression Artifacts**: ie the visual distorions present when an image is compressed , leveraging the JPEG format's lossy compression.
   - **Adding Noise**: Minimal Gaussian noise was added to slightly modify the image

2. **Trade-offs Considered**:
   - **Search Space Size**: Computational complexity grows exponentially with prefix length.
   - **Computation Time**: The proof-of-concept performs one iteration to demonstrate feasibility.
   - **Visual Fidelity**: Ensuring changes remain non-visible by altering the mentioned components.

3. **Simulated Annealing**: This optimization technique was chosen as it explores the search space by:
   - Initially making broader, random changes.
   - Gradually narrowing modifications as it approaches the desired hash.

4. **Theoretical Basis**:
   -Using JPG/JPEG format for its tolerance to changes due to lossy compression
   - Using SHA-256 as the hash algorithm ensures:
     - Moderate speed.
     - A manageable search space (e.g., 256 iterations for a 2-character prefix).
     
---


## Key Features

- Accepts the following as command line arguments: a JPG/JPEG image , arbitrary valid hexstring , output JPG/JPEG image
- Creates a hash of the input image
- Adds hexstring prefix to image hash and rearranges resulting hash to maintain image appearance
- Turns final hash into output image
- Saves modified image as output


### Folder Structure

```plaintext
spoof-woof/
|--- __pycache__ - Stores compiled bytecode files (.pyc) for Python modules.
|--- bin/
|--- lib/ - Stores the site-packages and standard library for the virtual environment.
|--- .gitignore - Ommits files/folders
|--- .README.md - project background and guide
|--- .altered.jpg - final output image, can be overwritten
|--- lib64 - A symbolic link to lib on 64-bit systems
|--- original.jpg - input image
|--- pyvenv.cfg -  Configuration file for the virtual environment.
|--- requirements.txt - stores project dependencies
|--- spoof.py - main python file
|--- test_spoof.py -test
```
### Main modules
**Image Input and Saving** - Handles processing images input via command-line arguments,validating the other inputs passed and saving the output image.
**Image Modification** - Contains methods used to modify the input image including modifying insignifcant bits,adding small amounts of noise, modyifing compression artifacts and EXIF data 
**Search (Simulated Annealing)** - Shows the search process which involves appending the target prefix to the image hash and applying image modifications to match the desired hash.The algorithm starts with a high level of randomness (high temperature) to explore the search space broadly.As the search progresses and approaches the desired hash, the randomness is gradually reduced (cooling), refining the results.


## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/)  installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/stephmukami/spoof-woof.git

# Go into the repository folder
$ cd spoof-woof

# Activate virtual environment
$ source bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Run the app, use any valid hexstring
$ python spoof.py 0x24 original.jpg altered.jpg


```

> **Note**
> You can interact with the program via a UI built using streamlit, [Streamlit App](https://stephmukami-streamlit-spoof-streamlitmain-mbkzqu.streamlit.app/) 🎉

## Limitations
This solution **does not find the exact hash match for an arbitrary hexstring prefix** as it only undergoes one iteration as a proof of concept and also considering computational complexity. An exact match could be found by increasing the number of iterations or using more
sophisticated search optimization techniques like [Genetic Algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm#:~:text=In%20computer%20science%20and%20operations,hyperparameter%20optimization%2C%20and%20causal%20inference.) and other machine learning approaches.
## License

MIT
---
## Technical Skills Gained
- Incorporating third-party Python libraries like piexif or Pillow for image manipulation.
- Creating and deploying apps using UI libraries like Streamlit
- Debugging Streamlit-specific issues and other errors.
- Testing using PyTest
- Problem Solving


