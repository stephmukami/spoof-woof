
<h1 align="center">
  Image Hash Spoofing
  <br>
</h1>

<h4 align="center">A solution for image hash spoofing.</h4>
<p align="center">
  <a href="#background-ideation">Background and Ideation</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#code-explanation">Code Explanation</a> •
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
   - **Compression Artifacts**: Leveraging the JPEG format's lossy compression.

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
## Code Explanation
> **Note**
> You can interact with the program via a UI built using streamlit, [Streamlit App](https://stephmukami-streamlit-spoof-streamlitmain-mbkzqu.streamlit.app/)

## License

MIT

---
## Technical Skills Gained
- Incorporating third-party Python libraries like piexif or Pillow for image manipulation.
- Creating and deploying apps using UI libraries like Streamlit
- Debugging Streamlit-specific issues.
- Problem Solving

