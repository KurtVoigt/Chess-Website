from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Space, Board
from django.template import loader
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
pieces = {
    "wPawn" : "&#9817",
    "wKnight" : "&#9816",
    "wBishop" : "&#9815",
    "wRook" : "&#9814",
    "wQueen" : "&#9813",
    "wKing" : "&#9812",
    "bPawn" : "&#9823",
    "bKnight" : "&#9822",
    "bBishop" : "&#9821",
    "bRook" : "&#9820",
    "bQueen" : "&#9819",
    "bKing" : "&#9818"
}

def home(request):
    if request.method == 'GET':
        try: #get saved board
            board = Board.objects.get(board_name = "putUserNameHere")
        except: #or create new one
            board = Board(board_name="putUserNameHere")
            board.save()
            board.space_list.create(space_row="8", space_col="a", space_piece=pieces['bRook'])
            board.space_list.create(space_row="8", space_col="b", space_piece=pieces['bKnight'])
            board.space_list.create(space_row="8", space_col="c", space_piece=pieces['bBishop'])
            board.space_list.create(space_row="8", space_col="d", space_piece=pieces['bKing'])
            board.space_list.create(space_row="8", space_col="e", space_piece=pieces['bQueen'])
            board.space_list.create(space_row="8", space_col="f", space_piece=pieces['bBishop'])
            board.space_list.create(space_row="8", space_col="g", space_piece=pieces['bKnight'])
            board.space_list.create(space_row="8", space_col="h", space_piece=pieces['bRook'])

            board.space_list.create(space_row="7", space_col="a", space_piece=pieces['bPawn'])
            board.space_list.create(space_row="7", space_col="b", space_piece=pieces['bPawn'])
            board.space_list.create(space_row="7", space_col="c", space_piece=pieces['bPawn'])
            board.space_list.create(space_row="7", space_col="d", space_piece=pieces['bPawn'])
            board.space_list.create(space_row="7", space_col="e", space_piece=pieces['bPawn'])
            board.space_list.create(space_row="7", space_col="f", space_piece=pieces['bPawn'])
            board.space_list.create(space_row="7", space_col="g", space_piece=pieces['bPawn'])
            board.space_list.create(space_row="7", space_col="h", space_piece=pieces['bPawn'])

            board.space_list.create(space_row="1", space_col="a", space_piece=pieces['wRook'])
            board.space_list.create(space_row="1", space_col="b", space_piece=pieces['wKnight'])
            board.space_list.create(space_row="1", space_col="c", space_piece=pieces['wBishop'])
            board.space_list.create(space_row="1", space_col="d", space_piece=pieces['wKing'])
            board.space_list.create(space_row="1", space_col="e", space_piece=pieces['wQueen'])
            board.space_list.create(space_row="1", space_col="f", space_piece=pieces['wBishop'])
            board.space_list.create(space_row="1", space_col="g", space_piece=pieces['wKnight'])
            board.space_list.create(space_row="1", space_col="h", space_piece=pieces['wRook'])

            board.space_list.create(space_row="2", space_col="a", space_piece=pieces['wPawn'])
            board.space_list.create(space_row="2", space_col="b", space_piece=pieces['wPawn'])
            board.space_list.create(space_row="2", space_col="c", space_piece=pieces['wPawn'])
            board.space_list.create(space_row="2", space_col="d", space_piece=pieces['wPawn'])
            board.space_list.create(space_row="2", space_col="e", space_piece=pieces['wPawn'])
            board.space_list.create(space_row="2", space_col="f", space_piece=pieces['wPawn'])
            board.space_list.create(space_row="2", space_col="g", space_piece=pieces['wPawn'])
            board.space_list.create(space_row="2", space_col="h", space_piece=pieces['wPawn'])

            board.space_list.create(space_row="3", space_col="a", space_piece="")
            board.space_list.create(space_row="3", space_col="b", space_piece="")
            board.space_list.create(space_row="3", space_col="c", space_piece="")
            board.space_list.create(space_row="3", space_col="d", space_piece="")
            board.space_list.create(space_row="3", space_col="e", space_piece="")
            board.space_list.create(space_row="3", space_col="f", space_piece="")
            board.space_list.create(space_row="3", space_col="g", space_piece="")
            board.space_list.create(space_row="3", space_col="h", space_piece="")
        
            board.space_list.create(space_row="4", space_col="a", space_piece="")
            board.space_list.create(space_row="4", space_col="b", space_piece="")
            board.space_list.create(space_row="4", space_col="c", space_piece="")
            board.space_list.create(space_row="4", space_col="d", space_piece="")
            board.space_list.create(space_row="4", space_col="e", space_piece="")
            board.space_list.create(space_row="4", space_col="f", space_piece="")
            board.space_list.create(space_row="4", space_col="g", space_piece="")
            board.space_list.create(space_row="4", space_col="h", space_piece="")

            board.space_list.create(space_row="5", space_col="a", space_piece="")
            board.space_list.create(space_row="5", space_col="b", space_piece="")
            board.space_list.create(space_row="5", space_col="c", space_piece="")
            board.space_list.create(space_row="5", space_col="d", space_piece="")
            board.space_list.create(space_row="5", space_col="e", space_piece="")
            board.space_list.create(space_row="5", space_col="f", space_piece="")
            board.space_list.create(space_row="5", space_col="g", space_piece="")
            board.space_list.create(space_row="5", space_col="h", space_piece="")

            board.space_list.create(space_row="6", space_col="a", space_piece="")
            board.space_list.create(space_row="6", space_col="b", space_piece="")
            board.space_list.create(space_row="6", space_col="c", space_piece="")
            board.space_list.create(space_row="6", space_col="d", space_piece="")
            board.space_list.create(space_row="6", space_col="e", space_piece="")
            board.space_list.create(space_row="6", space_col="f", space_piece="")
            board.space_list.create(space_row="6", space_col="g", space_piece="")
            board.space_list.create(space_row="6", space_col="h", space_piece="")
            board.save()
        context = {
            'board' : board,
        }  
        return render(request, 'chessboardApp/home.html', context)
    if request.method == 'POST':
        board = Board.objects.get(board_name = "putUserNameHere")
        from_field = request.POST.get('fromTextBox')
        to_field = request.POST.get('toTextBox')
        if to_field=="" or from_field=="":
            context = {
            'board' : board,
            }  
            return render(request, 'chessboardApp/home.html', context)
        if to_field=="RESET" or from_field=="RESET":
            #context = {
            #'board' : board,
            #}
            return render(request, 'chessboardApp/home.html', context)
        fromSpace = board.space_list.filter(space_col=from_field[0]).filter(space_row=from_field[1])
        fromSpace = fromSpace[0]
        toSpace = board.space_list.filter(space_col=to_field[0]).filter(space_row=to_field[1])[0]
        toSpace.space_piece = fromSpace.space_piece
        fromSpace.space_piece = ""
        toSpace.save()
        fromSpace.save()
        board.save()
        
        context = {
            'board' : board,
        }  
        return render(request, 'chessboardApp/home.html', context)
def rules(request):
    return render(request, 'chessboardApp/rules.html')

def history(request):
    return render(request, 'chessboardApp/history.html')

def about(request):
    return render(request, 'chessboardApp/about.html')
def reset(request):
    try: #get saved board
        board = Board.objects.get(board_name = "putUserNameHere")
        board.delete()
    except:
        x=1
    board = Board(board_name="putUserNameHere")
    board.save()
    board.space_list.create(space_row="8", space_col="a", space_piece=pieces['bRook'])
    board.space_list.create(space_row="8", space_col="b", space_piece=pieces['bKnight'])
    board.space_list.create(space_row="8", space_col="c", space_piece=pieces['bBishop'])
    board.space_list.create(space_row="8", space_col="d", space_piece=pieces['bKing'])
    board.space_list.create(space_row="8", space_col="e", space_piece=pieces['bQueen'])
    board.space_list.create(space_row="8", space_col="f", space_piece=pieces['bBishop'])
    board.space_list.create(space_row="8", space_col="g", space_piece=pieces['bKnight'])
    board.space_list.create(space_row="8", space_col="h", space_piece=pieces['bRook'])

    board.space_list.create(space_row="7", space_col="a", space_piece=pieces['bPawn'])
    board.space_list.create(space_row="7", space_col="b", space_piece=pieces['bPawn'])
    board.space_list.create(space_row="7", space_col="c", space_piece=pieces['bPawn'])
    board.space_list.create(space_row="7", space_col="d", space_piece=pieces['bPawn'])
    board.space_list.create(space_row="7", space_col="e", space_piece=pieces['bPawn'])
    board.space_list.create(space_row="7", space_col="f", space_piece=pieces['bPawn'])
    board.space_list.create(space_row="7", space_col="g", space_piece=pieces['bPawn'])
    board.space_list.create(space_row="7", space_col="h", space_piece=pieces['bPawn'])

    board.space_list.create(space_row="1", space_col="a", space_piece=pieces['wRook'])
    board.space_list.create(space_row="1", space_col="b", space_piece=pieces['wKnight'])
    board.space_list.create(space_row="1", space_col="c", space_piece=pieces['wBishop'])
    board.space_list.create(space_row="1", space_col="d", space_piece=pieces['wKing'])
    board.space_list.create(space_row="1", space_col="e", space_piece=pieces['wQueen'])
    board.space_list.create(space_row="1", space_col="f", space_piece=pieces['wBishop'])
    board.space_list.create(space_row="1", space_col="g", space_piece=pieces['wKnight'])
    board.space_list.create(space_row="1", space_col="h", space_piece=pieces['wRook'])

    board.space_list.create(space_row="2", space_col="a", space_piece=pieces['wPawn'])
    board.space_list.create(space_row="2", space_col="b", space_piece=pieces['wPawn'])
    board.space_list.create(space_row="2", space_col="c", space_piece=pieces['wPawn'])
    board.space_list.create(space_row="2", space_col="d", space_piece=pieces['wPawn'])
    board.space_list.create(space_row="2", space_col="e", space_piece=pieces['wPawn'])
    board.space_list.create(space_row="2", space_col="f", space_piece=pieces['wPawn'])
    board.space_list.create(space_row="2", space_col="g", space_piece=pieces['wPawn'])
    board.space_list.create(space_row="2", space_col="h", space_piece=pieces['wPawn'])

    board.space_list.create(space_row="3", space_col="a", space_piece="")
    board.space_list.create(space_row="3", space_col="b", space_piece="")
    board.space_list.create(space_row="3", space_col="c", space_piece="")
    board.space_list.create(space_row="3", space_col="d", space_piece="")
    board.space_list.create(space_row="3", space_col="e", space_piece="")
    board.space_list.create(space_row="3", space_col="f", space_piece="")
    board.space_list.create(space_row="3", space_col="g", space_piece="")
    board.space_list.create(space_row="3", space_col="h", space_piece="")
        
    board.space_list.create(space_row="4", space_col="a", space_piece="")
    board.space_list.create(space_row="4", space_col="b", space_piece="")
    board.space_list.create(space_row="4", space_col="c", space_piece="")
    board.space_list.create(space_row="4", space_col="d", space_piece="")
    board.space_list.create(space_row="4", space_col="e", space_piece="")
    board.space_list.create(space_row="4", space_col="f", space_piece="")
    board.space_list.create(space_row="4", space_col="g", space_piece="")
    board.space_list.create(space_row="4", space_col="h", space_piece="")

    board.space_list.create(space_row="5", space_col="a", space_piece="")
    board.space_list.create(space_row="5", space_col="b", space_piece="")
    board.space_list.create(space_row="5", space_col="c", space_piece="")
    board.space_list.create(space_row="5", space_col="d", space_piece="")
    board.space_list.create(space_row="5", space_col="e", space_piece="")
    board.space_list.create(space_row="5", space_col="f", space_piece="")
    board.space_list.create(space_row="5", space_col="g", space_piece="")
    board.space_list.create(space_row="5", space_col="h", space_piece="")

    board.space_list.create(space_row="6", space_col="a", space_piece="")
    board.space_list.create(space_row="6", space_col="b", space_piece="")
    board.space_list.create(space_row="6", space_col="c", space_piece="")
    board.space_list.create(space_row="6", space_col="d", space_piece="")
    board.space_list.create(space_row="6", space_col="e", space_piece="")
    board.space_list.create(space_row="6", space_col="f", space_piece="")
    board.space_list.create(space_row="6", space_col="g", space_piece="")
    board.space_list.create(space_row="6", space_col="h", space_piece="")
    board.save()
    context = {
        'board' : board,
    }  
    return render(request, 'chessboardApp/home.html', context)
