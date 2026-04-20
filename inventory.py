#!.venv/bin/python3
import json
from database import Servidor, Dispositivo, session_servidores, session_dispositivos

def gerar_inventario():
    """ FUNÇÂO PARA GERAR O INVENTÀIO EM JSON PARA O ANSIBLE """
    servidores = session_servidores.query(Servidor).all()
    dispositivos = session_dispositivos.query(Dispositivo).all()

    lista_ip_serv = [srv.ip_addr for srv in servidores]
    lista_ip_disp = [disp.ip_addr for disp in dispositivos]

    mapeamento_hosts_srv = {s.ip_addr : {
        "ansible_user": s.user_root,
        "ansible_ssh_private_key_file": s.ssh_key
        } for s in servidores}

    mapeamento_hosts_disp = {disp.ip_addr: {
        "ansible_user": disp.user_root,
        "ansible_ssh_private_key_file": disp.ssh_key
    } for disp in dispositivos}

    # Base para o JSON
    inventario = {
        "servidores": {
            "hosts": lista_ip_serv
        },
        "roteadores": {
            "hosts": lista_ip_disp
        },
        "_meta": {
            "hostvars":
                {**mapeamento_hosts_srv, **mapeamento_hosts_disp}
        }
    }

    print(json.dumps(inventario, indent=2))

if __name__ == "__main__":
    gerar_inventario()