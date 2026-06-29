from IPython.display import display, Markdown, clear_output
import re


# A simple utility function to stream the response from the model and display it in real-time.
# stream_by: 'chunk' (default) or 'word' to stream word-by-word
def stream_response(model, messages, stream_by: str = "chunk"):
    response = ""

    for chunk in model.stream(messages):
        content = chunk.content or ""

        if stream_by == "word":
            # Split into tokens that preserve whitespace so we can stream words cleanly
            tokens = re.findall(r"\S+|\s+", content)
            for token in tokens:
                response += token
                clear_output(wait=True)
                display(Markdown(response))
        else:
            response += content
            clear_output(wait=True)
            display(Markdown(response))

    # Final display (ensure full content shown)
    clear_output(wait=True)
    display(Markdown(response))

    return response