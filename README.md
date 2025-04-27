# AI Chat Assistant (Streamlit + Gemini API)

A lightweight, fast, and free AI chatbot application built with **Python**, **Streamlit**, and **Gemini AI**.  
Designed for easy customization and quick deployment.

---

## ✨ Features

- 🚀 Built with **Python** for core logic
- 🖥️ Beautiful UI with **Streamlit**
- 🤖 **Gemini-2.0-Flash** AI integration using `google.generativeai`
- 💬 Interactive chat experience powered by `streamlit_chat`
- 🔥 Fully customizable system instruction
- 🆓 Free to use and modify for personal or educational projects

---

## 🛠️ How to Set Up

1. **Clone this Repository**

   ```bash
   git clone https://github.com/dassayanhya/AI-Chat-Assistant
   cd your-repo-name
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Your Gemini API Key**

   - Visit [Google AI Studio](https://aistudio.google.com/) and generate your **Gemini API Key**.
   - Add your API key where required in the project (as per your implementation).

4. **Customize the System Instruction**

   - Open the file `chat.py`.
   - Go to **Line 20**.
   - Replace the existing system instruction with your custom prompt.

   Example:

   ```python
   SYSTEM_PROMPT = "You are an expert coding assistant who explains in simple language."
   ```

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

---

## 📄 Important Notes

- This project uses **Gemini-2.0-Flash** model for fast and responsive AI performance.
- Make sure your API key is kept private and secure.
- This project is **FREE TO USE**. Feel free to fork, modify, and enhance it!
- Respect Google AI's usage limits and policies while using the API.

---


## 🙌 Credits

- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini API)](https://aistudio.google.com/)
- [streamlit-chat Component](https://github.com/AI-Yash/st-chat)

---

## 📜 License

This project is released under the **MIT License**.  
You're free to use, modify, and distribute it with proper attribution!

---
