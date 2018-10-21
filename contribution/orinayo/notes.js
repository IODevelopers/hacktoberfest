const fs = require('fs')

const fetchNotes = () => {
  try {
    let notesString = fs.readFileSync('notes-data.json')
    return JSON.parse(notesString)
  } catch (e) {
    return []
  }
}

const saveNotes = notes => {
  fs.writeFileSync('notes-data.json', JSON.stringify(notes))
}

const addNote = (title, body) => {
  let notes = []
  let newNote = {
    title,
    body
  }
  notes = fetchNotes()
  let duplicateNotes = notes.filter(({ title }) => title === newNote.title)
  if (duplicateNotes.length === 0) {
    notes.push(newNote)
    saveNotes(notes)
    return newNote
  }
}

const getAll = () => {
  return fetchNotes()
}

const getNote = noteTitle => {
  let notes = fetchNotes()
  let note = notes.filter(({ title }) => title === noteTitle)
  return note[0]
}

const removeNote = noteTitle => {
  let notes = fetchNotes()
  let filteredNotes = notes.filter(({ title }) => title !== noteTitle)
  saveNotes(filteredNotes)
  return notes.length !== filteredNotes.length
}

const logNote = ({ title, body }) => {
  console.log('--------')
  console.log(`Title: ${title}`)
  console.log(`Body: ${body}`)
}

module.exports = {
  addNote,
  getAll,
  getNote,
  removeNote,
  logNote
}
