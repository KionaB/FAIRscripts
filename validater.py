from pyshacl import validate

data_graph = "train-lending-club-filtered1000-csv.ttl"
shacl_graph = "shacl-train-lending-club-filtered1000-csv.ttl"
ont_graph = None

r = validate(data_graph,
      shacl_graph=shacl_graph,
      ont_graph=ont_graph,
      inference='rdfs',
      abort_on_first=False,
      allow_infos=False,
      allow_warnings=False,
      meta_shacl=False,
      advanced=False,
      js=False,
      debug=True)
conforms, results_graph, results_text = r
print(conforms)
print(results_graph)
print(results_text)