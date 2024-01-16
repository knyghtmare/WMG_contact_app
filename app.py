import streamlit as st
import requests

WEBHOOK_URL_WMG = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjUwNTY5MDYzZTA0MzM1MjZlNTUzMzUxM2Ei_pc"
logo_path = "imgs/wmg_logo.png"
bfw_path = "imgs/bfw_logo.png"

st.set_page_config(page_title="Wesnoth Modders Guild",
                   page_icon=":star:",
                   layout='wide')


def post_to_webhook(**data):
    """
    Function to post data to the webhook using argument unpacking
    """
    response = requests.post(WEBHOOK_URL_WMG, json=data)
    return response


# st.write(f"Webhook URL is: {WEBHOOK_URL_WMG}")
left, mid, right = st.columns([2, 6, 2])

with left:
    st.image(logo_path)

with right:
    st.image(bfw_path)

with mid:
    st.title("Wesnoth Modders Guild")
    st.subheader("Communication Messaging App on Streamlit")

    st.markdown("""Have something to say to the Wesnoth Modders Guild (WMG)? Drop a message here and we shall respond when we can! Any message sent here will go directly to the server where WMG members can see it.
    """
    )

    container = st.container()

    with container:
        with st.form(key="idea_form"):
            name = st.text_input("Name (optional)", placeholder="Your Name")
            contact_id = st.text_input("Contact (optional)", placeholder="Your Email/Discord/ForumID")
            message_text = st.text_area("Message Text", placeholder="Write your message here...")

            submit_button = st.form_submit_button(label="Send Message 🚀")

            if submit_button:

                if not message_text.strip():
                    st.error("Please type a message.")
                    st.stop()

                data = {"name": name, 
                        "contact_id": contact_id, 
                        "message_text": message_text}

                response = post_to_webhook(**data)

                if response.status_code == 200:
                    st.success("Thanks for your submission! 🌟")
                else:
                    st.error("There was an error. Please try again. 🛠️")


