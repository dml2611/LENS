import os
import collections
import onco_lens_ner as lens

BG_COLOR = {"TRT": "#997a8d", "SYM": "#db7093", "MET": "#ffb6c1", "CANC_T": "#e68fac", "SIZE": "#fc89ac", "EMO": "#f78fa7", "PPL": "#dea5a4", "MED": "#e18e96",
                          "MHD": "#ff91af", "ORG": "#ff91a4", "ADV_EFF": "#f19cbb", "INV": "#efbbcc", "POB": "#F9CBCB", "EGY": "#e8ccd7", "DUR": "#f7bfbe", "AGE": "#c4c3d0",
                          "GENDER": "#ffc1cc", "STG": "#aa98a9", "EXP": "#d98695", "A/G": "#dea5a4", "RES": "#cc8899", "DIAG": "#fc6c85", "GPE": "#c9c0bb", "NUM": "#e5ccc9"}

# format a typical entity for display 
def format_entity(token, tag):
  if tag:
    start_mark = f'<mark class="entity" style="background: {BG_COLOR[tag]}; padding: 0.4em 0.4em; margin: 0 0.25em; line-height: 0.8; border-radius: 0.25em;">'
    end_mark = '\n</mark>'
    start_span = '<span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">'
    end_span = '\n</span>'
    return f"\n{start_mark}{token}{start_span}{tag}{end_span}{end_mark}"
  return f"{token}"

# extract all known entities in a lists
def get_token_tags(txtstr, entities):
  begin, tokens_tags = 0, []
  for start, vals in entities.items():
    length, ent, tag = vals
    if begin <= start:
      tokens_tags.append((txtstr[begin:start], None))
      tokens_tags.append((txtstr[start:start+length], tag))
      begin = start+length
  tokens_tags.append((txtstr[begin:], None)) #add the last untagged chunk
  return tokens_tags

def visualize(text, ents):
  html, end_div = f'<div class="entities" style="line-height: 2.3; direction: ltr">', '\n</div>'
  for token, tag in get_token_tags(text, ents):
    html += format_entity(token,tag)
  html += end_div
  return html

# merge two entities
def merge_entities(first_ents, second_ents):
  return collections.OrderedDict(
      sorted({** second_ents, **first_ents}.items()))

# show text unformated text
def show_plain_text(txtstr):
  'Original text:'
  start_mark = f'<mark class="entity" style="background: #FFFFFF; line-height: 2; border-radius: 0.35em;">'
  end_mark = '\n</mark>'
  return f"{start_mark}{txtstr}{end_mark}"

#=============================  Building the Spacy model  ===================================

EXAMPLES_DIR = os.path.join('resources', 'example_texts')

example_files = sorted([f for f in os.listdir(EXAMPLES_DIR) if f.endswith('.txt')])
