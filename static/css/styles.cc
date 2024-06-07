body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f0f0f0;
}

h1 {
    margin-top: 20px;
}

.game-board {
    display: grid;
    grid-template-columns: repeat(4, 100px);
    grid-gap: 10px;
    justify-content: center;
    margin-top: 20px;
}

.card {
    width: 100px;
    height: 100px;
    background-color: #2e3b4e;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    position: relative;
    border-radius: 10px;
}

.card.flipped,
.card.matched {
    background-color: #fff;
}

.card img {
    width: 80%;
    height: 80%;
    display: none;
}

.card.flipped img,
.card.matched img {
    display: block;
}
