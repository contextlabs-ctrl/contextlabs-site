import streamlit as st

# -------------------- Page Setup --------------------
st.set_page_config(page_title="ContextLabs — AI/NLP Engineer", layout="wide")

# Allow iframe embedding explicitly
st.markdown(
    "<style>iframe {width:100%; height:100%;}</style>",
    unsafe_allow_html=True
)

# -------------------- Header --------------------
st.title("🧠 Context Labs")
st.subheader("AI/NLP Engineer | LLM Specialist | Freelance + Full-Time Roles")

st.markdown("""
Welcome! I'm an AI engineer focused on building real-world applications with Large Language Models (LLMs).
Whether you're looking for freelance help, a team member, or a custom AI assistant — let's connect.
""")

st.markdown("---")

# -------------------- About Section --------------------
st.header("About Me")
st.markdown("""
I have a PhD in Computer Science and over 20 years of experience in software engineering, with a recent focus on NLP and LLMs.

What I do:
- Build custom document assistants (summarization, Q&A, chat over files)
- Work with GPT, DeepSeek, HuggingFace models
- Design clean UX with Streamlit + LangChain-style architectures

I'm currently open to:
- Freelance & contract projects
- Full-time AI/NLP roles (remote or hybrid)
""")

st.markdown("---")

# -------------------- Projects Section --------------------
st.header("Featured Project")
st.subheader("AI Document Assistant")
st.markdown("""
A multi-purpose tool that lets you upload a document and either:
- Summarize it based on document type and business purpose
- Ask questions directly to the content

It supports multiple LLMs: GPT-3.5, DeepSeek, Zephyr, Falcon — and smart prompt building.
""")

st.markdown("[Open the Demo App >](https://clabs-ai-doc-assistant.streamlit.app/)")

st.markdown("---")

# -------------------- Contact Section --------------------
st.header("Contact")
st.markdown("""
Let's work together!

📧 Email: ali@contextlabs.dev  
🔗 [LinkedIn](https://www.linkedin.com/in/aliakbar-keshtkaran/)  
💻 [GitHub](https://github.com/aak1983)
""")

# -------------------- Footer --------------------
st.markdown("""
---
Built with ❤️ using Streamlit.  
© 2025 ContextLabs
""")
