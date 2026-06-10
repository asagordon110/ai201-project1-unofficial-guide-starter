import gradio as gr
from query import ask


def handle_query(question):
    result = ask(question)

    answer = result["answer"]

    sources = "\n".join(
        f"• {source}"
        for source in result["sources"]
    )

    return answer, sources


with gr.Blocks() as demo:

    gr.Markdown(
        "# UTSA Unofficial Student Guide"
    )

    question = gr.Textbox(
        label="Ask a Question"
    )

    ask_button = gr.Button("Ask")

    answer = gr.Textbox(
        label="Answer",
        lines=8
    )

    sources = gr.Textbox(
        label="Sources",
        lines=4
    )

    ask_button.click(
        handle_query,
        inputs=question,
        outputs=[answer, sources]
    )

demo.launch()