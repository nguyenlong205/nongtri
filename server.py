from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key="AIzaSyDt3AbmnJS1JIYGuG7fJk-bm75wCJn8f8U")

while True:
    user_input = input("Nhập câu hỏi của bạn (nhập 'exit' để thoát): ")
    if user_input.strip().lower() == "exit":
        break
    # Streaming kết quả từng phần
    for chunk in llm.stream(user_input):
        print(chunk.content, end="")
    print("\n")  # Xuống dòng sau khi hoàn thành streaming
    
