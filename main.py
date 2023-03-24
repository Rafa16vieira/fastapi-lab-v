from fastapi import FastAPI
from fastapi import HTTPException, status
from models import Post
app = FastAPI()

@app.get("/home")
async def titulo():
    post = titulo[1]
    return post

@app.get("/posts")
async def listar_posts():
    return posts

@app.get('/posts/{post_id}')
async def detalhar_post(post_id: int):
    try:
        post = posts[post_id]
        return post
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Produto inexistente.')
    
@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def post_curso(post:Post):
    id = len(posts) + 1
    posts[id] = post
    return post


@app.delete('/posts/{post_id}')
def deletar_post(post_id: int):
    try:
        del posts[post_id]
        return {"msg": "produto deletado"}
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Produto inexistente.')


@app.put('/posts/{post_id}')
def atualizar_post(post_id: int, post: Post):
    posts[post_id] = post
    return {"msg": "produto atualizado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

posts = {
    1: {
        'livro': 'Harry Potter e a Pedra Filosofal'
    },
    2: {
        'livro': 'Harry Potter e a Câmara Secreta'
    },
    3: {
        'livro': 'Harry Potter e o Prisioneiro de Azkaban'
    }
}

titulo = {
    1: {
        'titulo': 'Livraria 4:20'
    }
}