import yaml
from jinja2 import Environment



print("Loading data...")
data = yaml.load(open("./website/data.yaml", Loader=yaml.FullLoader))
env = Environment(extensions=["jinja_markdown.MarkdownExtension"])

print("Importing template...")
template = env.from_string(
    open("./website/template.html").read()
)

print("Rendering index.html...")
output = template.render(**data)
open("./website/index.html", "w").write(output)

print("Website generated!")