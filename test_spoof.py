import pytest
from unittest.mock import patch, MagicMock
from spoof import main
import PIL.Image

# Test for hexstring missing prefix
def test_hexstring_missing_prefix():
    with patch("sys.argv", ["spoof.py", "12345", "input.jpg", "output.jpg"]):
        with pytest.raises(SystemExit):
            main()


# Test for hexstring with invalid characters
def test_hexstring_invalid_characters():
    with patch("sys.argv", ["spoof.py", "0xg12f", "input.jpg", "output.jpg"]):
        with pytest.raises(SystemExit):
            main()


# Test for invalid image format
def test_image_format_validation():
    with patch("sys.argv", ["spoof.py", "0x1234", "input.txt", "output.jpg"]):
        with patch("PIL.Image.open") as mock_open:
            mock_image = MagicMock()
            mock_image.format = "TXT"  
            mock_open.return_value = mock_image
            with pytest.raises(SystemExit):
                main()

# Test opening an image and calling simulated_annealing without saving the image.
def test_image_processing_open_and_annealing():
    with patch("sys.argv", ["spoof.py", "0x123456f", "input.jpg", "output.jpg"]):
        with patch("PIL.Image.open") as mock_open:
            mock_image = MagicMock(spec=PIL.Image.Image)
            mock_image.format = "JPEG"
            mock_open.return_value = mock_image  

            with patch("spoof.simulated_annealing") as mock_annealing:
                main() 

                mock_annealing.assert_called_once_with(mock_image, "0x123456f")

# Test if simulated_annealing processes the image and returns a new image.
def test_simulated_annealing_returns_image():
    with patch("sys.argv", ["spoof.py", "0x123456f", "input.jpg", "output.jpg"]):
        with patch("PIL.Image.open") as mock_open:
            mock_image = MagicMock(spec=PIL.Image.Image)
            mock_image.format = "JPEG"
            mock_open.return_value = mock_image  

            with patch("spoof.simulated_annealing", return_value=mock_image) as mock_annealing:
                main()  

                mock_annealing.assert_called_once_with(mock_image, "0x123456f")
# Test for invalid image path
def test_invalid_image_path():
    with patch("sys.argv", ["spoof.py", "0x1234", "non_existent_file.jpg", "output.jpg"]):
        with pytest.raises(SystemExit):  
            main()
