from altair import themes
import pandas as pd
import streamlit as st
import time
from PIL import Image
from io import BytesIO
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# CSS
st.markdown("""
    <style>
    .button-like {
        display: block;
        padding: 10px 20px;
        margin: 5px 0;
        font-size: 16px;
        color: white;
        background-color: #05192D;
        border: none;
        border-radius: 5px;
        text-align: center;
        text-decoration: none;
        cursor: pointer;
    }
    .button-like:hover {
        background-color: #074a76;
    }
    .bttn {
        display: block;
        padding: 10px 15px;
        margin: 5px 0;
        font-size: 15px;
        color:  #fafafa ;
        background-color: #05192D ;
        border: none ;
        border-radius: 10px;
        text-align: center;
        text-decoration: none;
        cursor: pointer;
    }
    .bttn:hover{
        color:  #1ED760 ;
    }
    </style>
""", unsafe_allow_html=True)



with st.sidebar:
    st.image(
        "C:/Users/Tsieb/Desktop/FOLDERS/PFC/NST_App/pic/Artboard 42.jpg",
        width=None,
    )
    with st.expander("HOME !"):
        st.markdown('''
        <a href="#what-is-nst" class="button-like">What Is NST!</a>
        <a href="#examples-and-gallery" class="button-like">Examples And Gallery</a>
        <a href="#share-your-art" class="button-like">Share Your Art!</a>
        ''', unsafe_allow_html=True)
    
    with st.expander("TRY IT NOW !:art:"):
       st.markdown('''
        <a href="#try-it-now" class="button-like">Try It Now!</a>
       ''', unsafe_allow_html=True)

    with st.expander("About Section"):
         st.markdown('''
        <a href="#About-Section" class="button-like">About Section!</a>
        <a href="#faq" class="button-like">FAQ & Help!</a>
       ''', unsafe_allow_html=True)
    
    with st.expander("Feedbacks & Rating :"):
       st.markdown('''
        <a href="#feedback" class="button-like">Feedbacks!</a>
        <a href="#rate" class="button-like">Rate this website!</a>
       ''', unsafe_allow_html=True)
    
    with st.expander("Our Contact:"):
       st.markdown('''
        <a href="#contact" class="button-like">Contact Us !</a>
       ''', unsafe_allow_html=True)


st.image(
    "C:/Users/Tsieb/Desktop/FOLDERS/PFC/PNG/Artboard 42.png",
      width=None,
)


# Title and description
st.title("Welcome to Our Neural Style Transfer Website! :sparkles:")
st.write("Get started now and experience the magic of neural style transfer!")

# Learning more section (static text for now)
st.write("Read about the fascinating world of neural style transfer and its applications.")
st.write("[Learn more...!](https://www.google.com/search?q=Neural+Style+Transfer&oq=Neural+Style+Transfer&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg7MgYIAhBFGEEyBggDEEUYPDIGCAQQRRhBMgYIBRBFGDwyBggGEC4YQNIBCDgxMjJqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8)")




st.video("https://youtu.be/DfLgBga2Vek?si=GY9Cwl8cAbNrZBrG")

# Separator (use st.write() with a horizontal rule markdown)
st.write("---")

# What is Neural Style Transfer section
st.subheader("What Is Neural Style Transfer ! :thinking_face:")
st.markdown('<a id="what-is-nst"></a>', unsafe_allow_html=True)

st.markdown("**The Neural Style Transfer** model allows you to transform your photos into stunning works of art with just a few clicks!")


coll1, coll2 , coll3 = st.columns(3)

with coll1:
    st.image(f"C:/Users/Tsieb/Desktop/FOLDERS/PFC/PNG/Artboard 72.png",
        width=180,) # Set width of each image 

with coll2:
   st.image(f"C:/Users/Tsieb/Desktop/FOLDERS/PFC/PNG/Artboard 62.png",
        width=180,) # Set width of each image 
with coll3:
   st.image(f"C:/Users/Tsieb/Desktop/FOLDERS/PFC/PNG/Artboard 82.png",
        width=180,) # Set width of each image 
   

st.markdown("<a href='#examples-and-gallery' class='bttn'>... See more examples ...</a>", unsafe_allow_html=True)
st.write("\n")

with st.expander("HOW NST WORKS"):
    st.write(
        """
        # Neural Style Transfer (NST)

        NST is a technique used in artificial intelligence and image processing to apply the style of one image (the "style image") to the content of another image (the "content image"), creating a new image that combines the content of the content image with the style of the style image.

        **Here's a simplified explanation of how NST works:**\n
        """
    )

    st.write(
        """
        **1. Preprocessing:**\n
        Both the content and style images are initially processed to extract their respective content and style features. This typically involves using a pre-trained convolutional neural network (CNN), such as VGG or ResNet, to extract features at different layers of the network.
            """
    )
    st.code(
        """
        # Example code for preprocessing
        content_image = preprocess_content_image(content_path)
        style_image = preprocess_style_image(style_path)
        """
    )

    st.write("---")

    st.write(
        """
        **2. Content Representation:**\n
        The content features of the content image are extracted from one of the middle layers of the CNN. These features represent the high-level content information of the image, capturing things like shapes, objects, and their arrangement.
        """
    )
    st.code(
        """
        # Example code for extracting content features
        content_features = extract_content_features(content_image, cnn_model)
        """
    )

    st.write("---")

    st.write(
        """
        **3. Style Representation:**\n
        Similarly, the style features of the style image are extracted from multiple layers of the CNN. However, instead of focusing on the content of the image, these features capture the texture, color, and visual patterns present in the style image.
        """
    )
    st.code(
        """
        # Example code for extracting style features
        style_features = extract_style_features(style_image, cnn_model)
        """
    )

    st.write("---")

    st.write(
        """
        **4. Loss Functions:**\n
        NST uses loss functions to iteratively adjust the pixels of a generated image until it minimizes two types of loss:

        - **Content Loss:**\n
        Measures the difference between the content features of the generated image and the content features of the content image. This encourages the generated image to retain the same content as the content image.

        - **Style Loss:**\n
        Measures the difference between the style features of the generated image and the style features of the style image. This encourages the generated image to adopt the same style as the style image.
        """
    )
    st.code(
        """
        # Example code for calculating content loss
        content_loss = calculate_content_loss(content_features, generated_features)
        
        # Example code for calculating style loss
        style_loss = calculate_style_loss(style_features, generated_features)
        """
    )


    st.write("---")


    st.write(
        """
        **5. Optimization:**\n
        Through an optimization process, such as gradient descent, the pixel values of a generated image are adjusted to minimize both the content loss and the style loss simultaneously. This process continues iteratively until a satisfactory result is achieved.
        """
    )
    st.code(
        """
        # Example code for optimization
        generated_image = optimize_image(content_image, style_image, cnn_model)
        """
    )

    st.write("---")

    st.write(
        """
        **6. Post-processing:**\n
        Once the optimization process is complete, the generated image is often subjected to post-processing steps, such as denoising or smoothing, to enhance its visual quality.
        """
    )
    st.code(
        """
        # Example code for post-processing
        final_image = post_process_image(generated_image)
        """
    )


       
#if st.button("TRY IT NOW !"):
   # st.markdown('<a href="#try-it-now"></a>', unsafe_allow_html=True)


   


#col1, col2 = st.columns(2)

# Button 1
#with col1:
#    st.write("[See more examples ...](#examples-and-gallery)")

# Button 2
# with col2:
#    st.button("[TRY IT NOW !](#try-it-now)")

# st.write("Explore the technical details behind neural style transfer and how it creates unique stylized images.")
# st.write("[See more examples](example_url)")  # Replace with actual example URL

# Separator




st.write("---")





# Try it now section
st.subheader("TRY IT NOW !:art:")
st.markdown('<a id="try-it-now"></a>', unsafe_allow_html=True)

st.write("Whether you're an aspiring artist, a photography enthusiast, or simply looking to add a touch of flair to your images, you've come to the right place!")
st.write("Upload your favorite style and content images and watch as our AI technology combines them to create unique stylized masterpieces!")

# Image upload functionality (replace with actual file upload components)
st.subheader("Upload Your Images :inbox_tray:")
uploaded_style_image = st.file_uploader("Upload Style Image", type="jpg")
uploaded_content_image = st.file_uploader("Upload Content Image", type="jpg")

col1, col2 = st.columns(2)

# Button to trigger style transfer (for now, just displays a message)
if st.button("Start Now!"):
    if uploaded_style_image is not None and uploaded_content_image is not None:
        st.write("Great! Click 'See Results' below to see your stylized image.")
        col1.image(uploaded_style_image, caption='Style Image', use_column_width=True , width=300)
        col2.image(uploaded_content_image, caption='Content Image', use_column_width=True , width=300)

             # Simulate processing with a progress bar
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)  # Simulate processing time
            progress_bar.progress(percent_complete + 1)
        
        # Try it again button
        if st.button("Try it again"):
            uploaded_style_image = None
            uploaded_content_image = None

    else:
        st.write("Please upload both style and content images.")




st.write("---")



# Results section (static text for now)
st.subheader("Examples And Gallery")
st.markdown('<a id="examples-and-gallery"></a>', unsafe_allow_html=True)

st.write("Browse through our gallery of amazing stylized images created using our neural style transfer model!")

col1, col2 , col3 , col4 = st.columns(4)

with col1:
    st.image("C:/Users/Tsieb/Desktop/FOLDERS/AI/madrid/PNG/a13.png",
        width=170,) # Set width of each image 
with col2:
   st.image("C:/Users/Tsieb/Desktop/FOLDERS/AI/madrid/PNG/a23.png",
        width=170,) # Set width of each image 
with col3:
   st.image("C:/Users/Tsieb/Desktop/FOLDERS/AI/madrid/PNG/a33.png",
        width=170,) # Set width of each image 
with col4:
   st.image("C:/Users/Tsieb/Desktop/FOLDERS/AI/madrid/PNG/a43.png",
        width=170,) # Set width of each image 
   

col1, col2 , col3 , col4 = st.columns(4)

with col1:
    st.image(f"https://via.placeholder.com/300x200/FF5733/FFFFFF/?text=Example+Image+{1}",
        width=170,) # Set width of each image 

with col2:
   st.image(f"https://via.placeholder.com/300x200/FF5733/FFFFFF/?text=Example+Image+{2}",
        width=170,) # Set width of each image 
with col3:
   st.image(f"https://via.placeholder.com/300x200/FF5733/FFFFFF/?text=Example+Image+{3}",
        width=170,) # Set width of each image 
with col4:
   st.image(f"https://via.placeholder.com/300x200/FF5733/FFFFFF/?text=Example+Image+{4}",
        width=170,) # Set width of each image 
   


# Horizontal scrolling container
# st.write('<div style="display: flex; flex-direction: row; overflow-x: auto;">', unsafe_allow_html=True)

# Display only four images
# for i in range(4):  # Change the number to 4
   # st.image(
       # f"https://via.placeholder.com/300x200/FF5733/FFFFFF/?text=Example+Image+{i+1}",
      #  width=300,  # Set width of each image
   # )

#st.write('</div>', unsafe_allow_html=True)

#st.button("[Try it now!](example_url)")  # Replace with actual example URL
st.markdown('<a href="#try-it-now" class="bttn">TRY IT NOW!</a>', unsafe_allow_html=True)

# Separator


st.write("---")


# Call to action (consider adding a social media sharing component)
st.subheader("Share Your Art ! :eyes:")
st.markdown('<a id="share-your-art"></a>', unsafe_allow_html=True)

st.write("Spread the word and inspire others with your creations!")

#uploaded_art_image = st.file_uploader("Upload Your Art", type="jpg")

# Initialize session state to store uploaded images
if 'shared_images' not in st.session_state:
    st.session_state['shared_images'] = []

# Function to get image size
def get_image_size(image):
    width, height = image.size
    return width, height

# Function to convert image to base64
def image_to_base64(image_bytes):
    buffered = BytesIO(image_bytes)
    base64_encoded = base64.b64encode(buffered.getvalue()).decode()
    return base64_encoded

# Function to convert base64 to image
def base64_to_image(b64_string):
    decoded_img = base64.b64decode(b64_string)
    img = Image.open(BytesIO(decoded_img))
    return img


# Function to save image to file
def save_image(image_bytes, filename):
    with open(filename, "wb") as f:
        f.write(image_bytes)


uploaded_art_image = st.file_uploader("Upload Your Art", type="jpg")

if st.button("Share Now"):
    if uploaded_art_image is not None:
        image_bytes = uploaded_art_image.read()
        # Generate unique filename
        filename = f"shared_image_{len(st.session_state['shared_images'])}.jpg"
        save_image(image_bytes, filename)
        st.session_state['shared_images'].append(filename)
        st.write("Thank you for sharing your art!")
    else:
        st.write("Please upload an image to share.")

# Display shared images in a table
if st.session_state['shared_images']:
    st.subheader("Shared Art Gallery")

    num_cols = 3
    num_rows = 4

    col_width = int(12 / num_cols)

    for i in range(0, len(st.session_state['shared_images']), num_cols):
        images_row = st.session_state['shared_images'][i:i+num_cols]
        row = st.columns(num_cols)
        for j, filename in enumerate(images_row):
            with row[j % num_cols]:
                image = Image.open(filename)
                st.image(image, use_column_width=True)

st.write("---")


#About Section-------
st.subheader("About Section :")
st.markdown('<a id="About-Section"></a>', unsafe_allow_html=True)
st.write(
    """
    Our neural style transfer model, named Artify, was developed by a team of AI enthusiasts passionate about exploring the intersection of art and technology. \n Using state-of-the-art deep learning techniques, we created Artify to empower users to transform their photos into stunning works of art effortlessly.
     """ 
)

with st.expander("Development Process:") :
 st.write(
    """
    **Development Process:**\n
    Artify was developed using *Python* and *TensorFlow* , a powerful open-source *machine learning framework*.\n We leveraged pre-trained *CNN models* , such as *VGG19* , as the backbone of our style transfer algorithm. The development process involved extensive experimentation, fine-tuning, and optimization to achieve high-quality stylized results.
    """
 )
 
with st.expander("Team Members :") :
 st.write(
    """
    **Team Members:**\n
    - Benaicha Mohamed Etaib : -----
    - Rebbouh Mohamed Lamin : ------
    """
 )

with st.expander("Notable Features :") :
 st.write(
    """
    **Notable Features:**\n
    - User-friendly interface for easy image stylization.
    - Customizable parameters to control the style transfer process.
    - Fast and efficient processing, allowing for real-time stylization of images.
    - Integration with popular social media platforms for seamless sharing of stylized images.

    """
 )

with st.expander("Achievements :") :
 st.write(
    """
    **Achievements:**\n
    - Featured in several AI and tech publications for its innovative approach to neural style transfer.
    - Received positive feedback from users worldwide for its intuitive design and impressive results.
    - Continuously updated with new features and improvements based on user feedback and emerging technologies.
    """
)


st.write("---")






st.subheader("FAQ And Help 	:thought_balloon: ")
st.markdown('<a id="faq"></a>', unsafe_allow_html=True)
st.write("""
         **Frequently Asked Questions:**
         """ )

with st.expander("Q: What is neural style transfer (NST)?") :
 st.write(" A: Neural style transfer is a technique that combines the content of one image with the style of another image, creating artistic images.")

with st.expander("Q: How does your NST model work?") :
 st.write(""" 
         A: Our NST model utilizes deep learning algorithms to extract content and style features from input images and combines them to generate stylized images.
         """ )

with st.expander("Q: Can I use my own content and style images with your model?") :
 st.write(""" 
          A: Yes, our model allows users to upload their own content and style images for stylization.
         """)
         


st.write("---")


st.subheader("Troubleshooting Tips:")
st.write("""
         - If you encounter issues with image upload or processing, please ensure that your internet connection is stable and try again.
         - If the stylized image does not meet your expectations, consider adjusting the style transfer parameters or trying different content and style images for better results.\n
         """)



st.write("---")



# Function to read the feedback file and return its contents
def read_feedback_file(file_path):
    try:
        with open(file_path, "r") as file:
            feedback_content = file.readlines()  # Read each line of the file as a list
        return feedback_content
    except FileNotFoundError:
        return []

st.subheader("Feedbacks :")
st.markdown('<a id="feedback"></a>', unsafe_allow_html=True)
st.write("""
         
   **We Want Your Feedback!**

    We value your input and suggestions for improving our website and neural style transfer model. If you have any feedback or ideas, please share them with us!

    **Please enter your feedback below:**

    """)

st.markdown("<div class='feedback-textarea'>Your Feedback:</div>", unsafe_allow_html=True)
feedback = st.text_area("Your Feedback:", "")
#st.write("<span style='color:red'>This text is red</span>", unsafe_allow_html=True)


if st.button("Submit Feedback"):
    # Save the feedback to a file or database
    with open("feedback.txt", "a") as file:
        file.write(feedback + "\n")
    st.success("Thank you for your feedback! We will review it shortly.")
 

 # Display feedback file contents
with st.expander("Feedback Received"):
 st.write(
    """
    ## Feedback Received

    Here are the feedback messages we've received so far:

    """
  )

 feedback_content = read_feedback_file("feedback.txt")
 feedback_df = pd.DataFrame({"Feedback": feedback_content[::-1]})  # Reverse the order of feedbacks
 st.write(feedback_df.head(5))

# Add a section to rate the website

# Initialize session state to keep track of total ratings
if 'total_stars' not in st.session_state:
    st.session_state['total_stars'] = 0
if 'total_ratings' not in st.session_state:
    st.session_state['total_ratings'] = 0

# Function to display star rating
def star_rating(rating):
    filled_star_color = "gold"  # Color of filled stars
    empty_star_color = "lightgray"  # Color of empty stars
    stars = f"<span style='color: {filled_star_color};'>★</span>" * int(rating) + \
            f"<span style='color: {empty_star_color};'>☆</span>" * (5 - int(rating))
    centered_stars = f"<div style='text-align: center; font-size: 30px;'>{stars}</div>"
    st.markdown(centered_stars, unsafe_allow_html=True)


st.subheader("Rate This Website:")
st.markdown('<a id="rate"></a>', unsafe_allow_html=True)
st.write("Please rate our website on a scale of 1 to 5:")

# Checkbox to select stars
selected_stars = st.slider("Rate our website", min_value=0, max_value=5, step=1)
# Display the selected star rating
# Button to submit the rating
if st.button("Submit Rating"):
    st.session_state['total_stars'] += selected_stars
    st.session_state['total_ratings'] += 1
    st.write(f"You rated this website {selected_stars} stars.")
    star_rating(selected_stars)

# Display the total stars and average rating
if st.session_state['total_ratings'] > 0:
    avg_rating = st.session_state['total_stars'] / st.session_state['total_ratings']
    st.write(f"Total stars given: {st.session_state['total_stars']}")
    st.write(f"Average rating: {avg_rating:.2f} stars")





st.write("---")



st.subheader("Contact Us :")
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.write("""
         For further assistance or inquiries, please feel free to contact us at support@artify.com.
         """)

with st.expander("Our Contact !"):
    st.write(
        """
        **LinkedIn :**\n
        - Benaicha Mohamed Etaib : [LinkedIn Profile](https://www.linkedin.com/in/mohamed-etaib-benaicha-757600254/)
        - Rebbouh Mohamed Lamin : [LinkedIn Profile](https://www.linkedin.com/in/mohamed-etaib-benaicha-757600254/)

        **Gmail :**\n
        - Benaicha Mohamed Etaib : [Email](mailto:benaicha@example.com)
        - Rebbouh Mohamed Lamin : [Email](mailto:rebbouh@example.com)

         **GitHub :**\n
        - Benaicha Mohamed Etaib : [GitHub](mailto:benaicha@example.com)
        - Rebbouh Mohamed Lamin : [GitHub](mailto:rebbouh@example.com)
        """
    )
        
        
    

st.write("---")



