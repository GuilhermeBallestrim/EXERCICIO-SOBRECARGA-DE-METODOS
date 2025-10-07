import os
import datetime


class GerarRelatorio:
    def Gerar(self, *paragrafos, **caracteristicas):
        corpo = "\n".join(paragrafos)

        if "titulo" in caracteristicas:
            corpo = f"{caracteristicas['titulo']}\n\n{corpo}"

        if "rodape" in caracteristicas:
            corpo = f"{corpo}\n\n{caracteristicas['rodape']}"

        if "metadados" in caracteristicas:
            corpo += "\n\nMetadados:"
            for chave, valor in caracteristicas["metadados"].items():
                corpo += f"\n{chave} - {valor}"

        return corpo


## -----------------------------------------------------------------------------------------------
## -----------------------------------------------------------------------------------------------


texto = GerarRelatorio.Gerar(
    "Parágrafo 1",
    "Parágrafo 2",
    titulo="Título",
    rodape="Rodapé",
    metadados={
        "Autor": os.environ.get("USERNAME"),
        "Data": datetime.datetime.today().strftime("%d/%m/%Y"),
        "Versão": 1.0,
    },
)