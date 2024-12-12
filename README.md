
<h1 align="center">
  Image Hash Spoofing
  <br>
</h1>

<h4 align="center">A solution for image hash spoofing.</h4>
<p align="center">
  <a href="#how-to-use">Background and Ideation</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#tech-skills">Technical Skills Gained</a> •
  <a href="#license">License</a>
</p>
<div align="center">
  
  <img src="https://github.com/stephmukami/kikwetu_store/blob/master/project_pictures/kikwet_2.PNG" alt="sign up page" width="400">
  <img src="https://github.com/stephmukami/kikwetu_store/blob/master/project_pictures/kikwetu_1.PNG" alt="checkout page" width="400">
</div>

## Background and Ideation

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
> You can interact with the program via a UI built using streamlit, [Streamlit App](https://stephmukami-streamlit-spoof-streamlitmain-mbkzqu.streamlit.app/)

## License

MIT

---
## Technical Skills Gained
- Array Manipulation
- State management
- Conditional rendering
