from pathlib import Path
import json

path = Path('../eq_data/past_month_eq_data.geojson')
content = path.read_text()
all_eq_data = json.loads(content)

path = Path('../eq_data/readable_past_month_eq_data.json')
readable_content = json.dumps(all_eq_data, indent=4)
path.write_text(readable_content)
