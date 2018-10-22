const yargs = require('yargs')

const notes = require('./notes')
let note
const title = {
  describe: 'Title of note',
  demand: true,
  alias: 't'
}
const body = {
  describe: 'Body of note',
  demand: true,
  alias: 'b'
}

const argv = yargs
  .command('add', 'Add a new note', {
    title,
    body
  })
  .command('list', 'List all notes')
  .command('read', 'Read a note', {
    title
  })
  .command('remove', 'Delete a note', {
    title
  })
  .help()
  .argv
let command = argv._[0]

switch (command) {
  case 'add':
    note = notes.addNote(argv.title, argv.body)
    if (note) {
      console.log('Note created')
      notes.logNote(note)
    } else {
      console.log('Note title taken')
    }
    break
  case 'list':
    let allNotes = notes.getAll()
    console.log(`Printing ${allNotes.length} note(s).`)
    allNotes.forEach(note => notes.logNote(note))
    break
  case 'read':
    note = notes.getNote(argv.title)
    if (note) {
      console.log('Note found')
      notes.logNote(note)
    } else {
      console.log('Note not found')
    }
    break
  case 'remove':
    let noteRemoved = notes.removeNote(argv.title)
    noteRemoved ? console.log('Note was removed')
      : console.log('Note not found')
    break
  default:
    console.log('Command not recognized')
}
