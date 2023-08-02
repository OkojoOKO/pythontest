from browser import document, html

def action(event):
    element = event.target
    value = element.text
    if value not in "=C":
        if result.text in ["0", "error"]:
            result.text = value
        else:
            result.text = result.text + value
    elif value == "C":
        result.text = "0"
    elif value == "=":
        try:
            result.text = eval(result.text)
        except:
            result.text = "error"

calc = html.TABLE()
calc <= html.TR(html.TH(html.DIV("0", id="result"), colspan=3) + html.TD("C"))
lines = ["789/", "456*", "123-", "0.=+"]
calc <= (html.TR(html.TD(x) for x in line) for line in lines)
document <= calc
result = document["result"]

for button in document.select("td"):
    button.bind("click", action)
