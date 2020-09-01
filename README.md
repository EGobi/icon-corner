# icon-corner ☦

Este é um script de interface gráfica em Python para a exibição permanente (até SIGTERM) de um ícone no monitor, sempre acima das outras. São dois scripts em Python e um em shell, sendo que você pode escolher qual dos dois usar. Um foi feito no Qt, o outro no Tk. Claro, você vai precisar editar os campos de geometria e do caminho da imagem para que se adequem à sua realidade. Vamos para as instruções, então:

Eu estarei usando o `iconTk` por ser mais fácil.
1. Edite a linha `self.img = PhotoImage(file = '/home/neko/Pictures/.Mãe de Deus.png')` para que contenha o caminho completo do arquivo onde a imagem está. Aliás, veja como eu ocultei o arquivo com o `.` para que eu não o apagasse por engano (afinal, eu limpo minhas pastas Desktop, Pictures e Downloads quase toda semana). O ícone que eu estou usando é [esse](https://i.mycdn.me/i?r=AyH4iRPQ2q0otWIFepML2LxRM7WAaqCQwlLEtE_VqlQcgg), mas você pode usar qualquer um.
2. A linha de baixo reduz o tamanho da imagem pela metade (2,2). Altere esse valor se seu ícone ficar muito pequeno ou muito grande, mas sempre use números inteiros e iguais em ambos os argumentos (x,y).
3. Agora vem a parte da geometria. Sério, eu não faço ideia de como deixar isso “automático” para se encaixar nos cantos de qualquer tela, então você vai ter que ir alterando os pixels por tentativa e erro até se adequar à sua. Como eu uso dois monitores, eu configurei três posições (`'253x350+1366+694'`, `'253x350+3033+694'` e `'253x350+0+1082'`) em que o ícone se desloca quando é clicado. Se você usa só um monitor, é só apagar o que tá no `elif` e alterar as resoluções; mas se quiser que ele tenha outros deslocamentos, é só ir adicionando mais `elif`s e aumentar o `self.pos`. Basicamente, os dois primeiros números (`253x350`) equivalem à resolução da imagem, e sempre devem ser os mesmos. Os outros dois são as cordenadas na tela. É só ir brincando com os números e ver no que dá.
4. Teste sempre pelo console com `python3 iconTk.py`, pois aí dá pra matar o programa com `CTRL+C`. No KDE, precisa passar o mouse por cima do ícone para que ele morra.
5. E é isso. Se você quiser que o ícone sempre apareça ao ligar o computador, é só criar um script com `python3 /caminho/do/arquivo/iconTk.py` na pasta de inicialização (no KDE é em `~/.config/autostart-scripts/`; no Windows, dê `Win+R` e navegue para `shell:startup`, o endereço vai estar na barra de endereços do explorer).

O único contra de usar o Tk é que, por algum motivo, uma barrinha branca fica sempre mostrando em cima do ícone. E foi por isso que eu refiz no Qt. Se você também se irritar com essa barrinha branca, é só usar o `iconQt.py`, o código dele é bem semelhante, mas com algumas diferenças:
1. Edite a linha `pixmap = QPixmap('/home/neko/Pictures/.Mãe de Deus.png').scaled(253, 350, Qt.KeepAspectRatio)` para que contenha o caminho completo do blá blá blá…
2. Para mudar o tamanho, você deve saber a resolução da imagem e dividi-la ou multiplicá-la para o tamanho desejado. O bom é que você pode especificar o tamanho exato que você quer (diferente do Tk). O `Qt.KeepAspectRatio` fica lá para que a proporção seja mantida.
3. Mesma coisa, mas a ordem aqui é outra. Primeiro vêm as duas cordenadas e depois a resolução (`1366, 694, 253, 350`).
4. Igual!
5. Igual!!
