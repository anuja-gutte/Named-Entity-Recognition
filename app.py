import gradio as gr
from transformers import pipeline

# Load lightweight NER model
ner = pipeline(
    "ner",
    model="elastic/distilbert-base-cased-finetuned-conll03-english",
    aggregation_strategy="simple"
)

# Function for Gradio
def detect_entities(text):

    if not text.strip():
        return "Please enter some text."

    results = ner(text)

    output = ""

    for item in results:
        output += (
            f"Entity: {item['word']}\n"
            f"Type: {item['entity_group']}\n"
            f"Score: {round(item['score'], 3)}\n"
            f"----------------------\n"
        )

    return output


# Gradio UI
with gr.Blocks() as demo:

    gr.Markdown("# Named Entity Recognition (NER)")
    gr.Markdown("Detect names, locations, organizations, etc.")

    text_input = gr.Textbox(
        label="Enter Text",
        placeholder="Type a sentence here...",
        lines=4
    )

    detect_button = gr.Button("Detect Entities")

    output_box = gr.Textbox(
        label="Detected Entities",
        lines=10
    )

    detect_button.click(
        fn=detect_entities,
        inputs=text_input,
        outputs=output_box
    )

# Launch app
demo.launch()