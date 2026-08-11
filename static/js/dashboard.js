//==================================================
// Badge
//==================================================

function badge(status){

    let classe="online";

    if(status==="OFFLINE")
        classe="offline";

    if(status==="NÃO CADASTRADO")
        classe="alerta";

    return `<span class="badge ${classe}">${status}</span>`;

}


//==================================================
// MikroTik
//==================================================

function atualizarMikroTik(mk){

    document.getElementById("mikrotik").innerHTML=`

        <div class="info">
            <span>Status</span>
            <strong>${badge(mk.status)}</strong>
        </div>

        <div class="info">
            <span>Modelo</span>
            <strong>${mk.modelo}</strong>
        </div>

        <div class="info">
            <span>RouterOS</span>
            <strong>${mk.routeros}</strong>
        </div>

        <div class="info">
            <span>CPU</span>
            <strong>${mk.cpu}%</strong>
        </div>

        <div class="info">
            <span>RAM</span>
            <strong>${mk.memoria}%</strong>
        </div>

        <div class="info">
            <span>Uptime</span>
            <strong>${mk.uptime}</strong>
        </div>

    `;

}



//==================================================
// Links
//==================================================

function atualizarLinks(lista){

    lista.forEach(link=>{

        let div=document.getElementById(link.nome.toLowerCase());

        if(!div)
            return;

        div.innerHTML=`

            <div class="info">
                <span>Status</span>
                <strong>${badge(link.status)}</strong>
            </div>

            <div class="info">
                <span>IP</span>
                <strong>${link.ip}</strong>
            </div>

            <div class="info">
                <span>Interface</span>
                <strong>${link.interface}</strong>
            </div>

            <div class="info">
                <span>Velocidade</span>
                <strong>${link.velocidade}</strong>
            </div>

        `;

    });

}



//==================================================
// Rede Cabeada
//==================================================

function atualizarSetores(lista){

    let html="";

    lista.forEach(setor=>{

        html+=`

            <tr>

                <td>${setor.nome}</td>

                <td>${badge(setor.status)}</td>

                <td style="font-size:22px">${setor.velocidade}</td>

            </tr>

        `;

    });

    document.getElementById("tabelaSetores").innerHTML=html;

}



//==================================================
// WiFi
//==================================================

function atualizarWifi(lista){

    let html="";

    lista.forEach(ap=>{

        html+=`

            <tr>

                <td>${ap.nome}</td>

                <td>${badge(ap.status)}</td>

                <td style="font-size:22px">${ap.velocidade}</td>

            </tr>

        `;

    });

    document.getElementById("tabelaWifi").innerHTML=html;

}



//==================================================
// Impressoras
//==================================================

function atualizarImpressoras(lista){

    let html="";

    lista.forEach(imp=>{

        html+=`

            <tr>

                <td>${imp.nome}</td>

                <td>${imp.setor}</td>

                <td>${imp.ip}</td>

                <td>${badge(imp.status)}</td>

                <td style="font-size:22px">${imp.velocidade}</td>

            </tr>

        `;

    });

    document.getElementById("tabelaImpressoras").innerHTML=html;

}



//==================================================
// Resumo
//==================================================

function atualizarResumo(dados){

    document.getElementById("linksResumo").innerHTML=

        dados.resumo.links_online + "/" +

        dados.resumo.links_total;


    document.getElementById("equipamentosResumo").innerHTML=

        dados.resumo.equipamentos_online + "/" +

        dados.resumo.equipamentos_total;


    document.getElementById("cpuResumo").innerHTML=

        dados.mikrotik.cpu + "%";


    document.getElementById("routerResumo").innerHTML=

        dados.mikrotik.status;

}



//==================================================
// Dashboard
//==================================================

async function atualizarDashboard(){

    try{

        let resposta=await fetch("/api/dashboard",{

            cache:"no-store"

        });

        let dados = await resposta.json();

        console.log("Resposta da API:", dados);

        if(!dados.sucesso){

            console.error("Erro:", dados.erro);

        return;

        }

        atualizarMikroTik(dados.mikrotik);

        atualizarLinks(dados.links);

        atualizarSetores(dados.setores);

        atualizarWifi(dados.wifi);

        atualizarImpressoras(dados.impressoras);

        atualizarResumo(dados);

        document.getElementById("ultimaAtualizacao").innerHTML=

            "Última atualização: " +

            dados.ultima_atualizacao;

    }

    catch(e){

        console.log(e);

    }

}



//==================================================
// Controle de atualização
//==================================================

let atualizando = false;


//==================================================
// Controle de atualização
//==================================================

let atualizacaoEmAndamento = false;


//==================================================
// Dashboard
//==================================================

async function atualizarDashboard(){

    // Impede duas consultas simultâneas
    if(atualizacaoEmAndamento){

        console.log("Atualização anterior ainda em andamento. Aguardando...");

        return;
    }

    atualizacaoEmAndamento = true;

    try{

        let resposta = await fetch("/api/dashboard",{

            cache:"no-store"

        });

        let dados = await resposta.json();

        console.log("Resposta da API:", dados);

        if(!dados.sucesso){

            console.error("Erro:", dados.erro);

            return;

        }

        atualizarMikroTik(dados.mikrotik);

        atualizarLinks(dados.links);

        atualizarSetores(dados.setores);

        atualizarWifi(dados.wifi);

        atualizarImpressoras(dados.impressoras);

        atualizarResumo(dados);

        document.getElementById("ultimaAtualizacao").innerHTML =

            "Última atualização: " +

            dados.ultima_atualizacao;

    }

    catch(e){

        console.error("Erro ao atualizar dashboard:", e);

    }

    finally{

        atualizacaoEmAndamento = false;

    }

}


//==================================================
// Inicialização
//==================================================

window.onload = function(){

    atualizarDashboard();

};


//==================================================
// Atualização
//==================================================

setInterval(function(){

    atualizarDashboard();

}, 10000);