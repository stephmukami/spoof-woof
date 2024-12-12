
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

> **Note**
> You can interact with the program via a UI built using streamlit, [Streamlit App](https://stephmukami-streamlit-spoof-streamlitmain-mbkzqu.streamlit.app/) 🎉

## Limitations
This solution **does not find the exact hash match for an arbitrary hexstring prefix** as it only undergoes one iteration as a proof of concept and also considering computational complexity. An exact match could be found by increasing the number of iterations or using more
sophisticated search optimization techniques like [Genetic Algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm#:~:text=In%20computer%20science%20and%20operations,hyperparameter%20optimization%2C%20and%20causal%20inference.) and other machine learning approaches.
## License

MIT
---
## DEMO

<div flex="column">
<img src= "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHVxZmk0bG94NDhhZWpvbXQ4eHo3eXJlOHNwczMzZm54N3RyZWR3ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/z1C0XCq8tCkLtnGEg1/giphy.gif" alt="gif page" width="400" height="400">

<img src= "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzhiZ20wdHhjeHR6MWt1dDRrcmc1azlhazY5NzQ2a3Jic2p5eDFneSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ekHNvjgIW64tucKsVH/giphy.gif" alt="gif page" width="400" height="400">

</div>
<img src= "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExODk4N2FzYnJ5bWIxdDVkeDkyOGE3YzFyajIxOGIyZmtqMDN3MzR6bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lAa8uFh2Bvwo4aYYGZ/giphy.gif" alt="gif page" width="500" height="500">

<img src= "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzhiZ20wdHhjeHR6MWt1dDRrcmc1azlhazY5NzQ2a3Jic2p5eDFneSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ekHNvjgIW64tucKsVH/giphy.gif" alt="gif page" width="400" height="400">
 
---
## Technical Skills Gained
- Incorporating third-party Python libraries like piexif or Pillow for image manipulation.
- Creating and deploying apps using UI libraries like Streamlit
- Debugging Streamlit-specific issues and other errors.
- Testing using PyTest
- Problem Solving


