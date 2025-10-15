from pyshacl import validate
import logging

data_graph = "train-lending-club-filtered1000-csv.ttl"
shacl_graph = "shacl-train-lending-club-filtered1000-csv.ttl"
ont_graph = None

logging.basicConfig(filename='validation.log',
                    filemode='w',
                    level=logging.DEBUG)

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
             debug=False)
conforms, results_graph, results_text = r

logging.info(str(conforms))
logging.info(str(results_graph))
logging.debug(str(results_text))
