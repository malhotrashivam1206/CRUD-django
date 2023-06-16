from django.shortcuts import render, get_object_or_404, redirect
from notes.models import Note
from .models import Note
from .forms import NoteForm

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_all')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})

def update_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('read_all')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/update_note.html', {'form': form})

def delete_note(request, note_id):
    # Retrieve the note object
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return redirect('read_all')  # Redirect to the read_all view if note doesn't exist

    # Delete the note
    note.delete()
    
    return redirect('read_all')

def read_all_notes(request):
    notes = Note.objects.all()
    return render(request, 'notes/read_all_notes.html', {'notes': notes})

def read_note_by_id(request, note_id):
    # Retrieve the note object or return a 404 error if it doesn't exist
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/read_note.html', {'note': note})
