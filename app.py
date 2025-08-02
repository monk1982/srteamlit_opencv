import streamlit as st
import cv2 as cv
import os

img_path = "static"
cam = None

#make shots directory to save pics
try:
    os.mkdir(img_path)
except OSError as error:
    pass

def setup_page():
    st.set_page_config(page_title="Streamlit Opencv")
    st.header("📸 ĐẶT MỘT CÂU HỎI VỀ BỨC ẢNH CỦA BẠN.", anchor=False, divider="blue")
    st.sidebar.header("Hướng dẫn", divider="rainbow")
    st.sidebar.write("1. Chụp ảnh")
    st.sidebar.write("2. Đặt câu hỏi về bức ảnh")
    hide_menu_style =   """
                        <style>
                        #MainMenu {visibility: hidden;}
                        </style>
                        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

def main():
    """
    1. Setup page
    2. Ask user to take a picture
    3. Submit to MLLM with a prompt
    4. Display response

    Returns
    -------
    None.
    """
    global cam
    cam = cv.VideoCapture(0)

    setup_page()
    enable = st.checkbox("Bật camera")
    if enable:                
            #cam = cv.VideoCapture(0)
            frame_placeholder = st.empty()
            while cam.isOpened():
                ret, frame = cam.read()
                if not ret:
                    st.write("Video Capture Ended")
                    break
                
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                frame_placeholder.image(frame,channels="RGB")       
    else:        
        if cam.isOpened():
            cam.release()        
        cv.destroyAllWindows()
        

    #camera_image = st.camera_input("Chụp ảnh",label_visibility="collapsed", disabled=not enable)
    #if camera_image is not None:
    #    img = Image.open(camera_image)
    #    img.save('capture_img.jpg')
    #    quest = st.text_input("Viết câu hỏi của bạn về bức ảnh","")
    #    if quest:
    #        client = genai.GenerativeModel(model_name='gemini-2.5-flash')
    #        response = client.generate_content([quest, img],
    #                                            generation_config= genai.types.GenerationConfig(temperature=2.0))
    #        response.resolve()
    #        st.markdown(response.text)

# Code chạy lệnh Python
if __name__ == '__main__':
    main()