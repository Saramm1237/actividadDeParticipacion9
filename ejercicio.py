from typing import Dict, Any


class AnalizadorLogs:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_logs(self) -> Dict[str, Any]:
        num_solicitudes_total = 0
        solicitudes_por_metodo = {}
        solicitudes_por_respuesta = {}
        tamano_total_respuesta = 0
        tamano_promedio_respuesta = 0
        num_solicitudes_por_url = {}

        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                # Procesar cada línea de log
                campos = linea.strip().split()
                if len(campos) != 7:
                    continue

                direccion_ip = campos[0]
                fecha_hora = campos[1] + " " + campos[2]
                metodo_http = campos[3]
                url = campos[4]
                codigo_respuesta = campos[5]
                tamano_respuesta = int(campos[6])

                num_solicitudes_total += 1
                solicitudes_por_metodo[metodo_http] = solicitudes_por_metodo.get(metodo_http, 0) + 1
                solicitudes_por_respuesta[codigo_respuesta] = solicitudes_por_respuesta.get(codigo_respuesta, 0) + 1
                tamano_total_respuesta += tamano_respuesta
                num_solicitudes_por_url[url] = num_solicitudes_por_url.get(url, 0) + 1

        tamano_promedio_respuesta = tamano_total_respuesta / num_solicitudes_total
        urls_mas_solicitadas = sorted(num_solicitudes_por_url.items(), key=lambda x: x[1], reverse=True)[:10]

        estadisticas = {
            "num_solicitudes_total": num_solicitudes_total,
            "solicitudes_por_metodo": solicitudes_por_metodo,
            "solicitudes_por_respuesta": solicitudes_por_respuesta,
            "tamano_total_respuesta": tamano_total_respuesta,
            "tamano_promedio_respuesta": tamano_promedio_respuesta,
            "urls_mas_solicitadas": urls_mas_solicitadas
        }

        return estadisticas


analizador = AnalizadorLogs("trafico.txt")
print(analizador.procesar_logs())
