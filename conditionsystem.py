import streamlit as st
import cv2
import numpy as np

def is_valid_image(image_file):
    try:
        # Convert the file to an opencv image
        file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        if img is None:
            return False, "Invalid: Unable to read image file."

        # Add your image validation criteria here
        # For example, checking if the image has a certain width and height
        height, width, _ = img.shape
        if width < 100 or height < 100:
            return False, "Invalid: Image dimensions are too small."

        return True, "Valid"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    st.title("Image Validator")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        # Reset the file pointer to the beginning of the file
        uploaded_file.seek(0)
        is_valid, message = is_valid_image(uploaded_file)
        st.write(message)

if __name__ == "__main__":
    main()