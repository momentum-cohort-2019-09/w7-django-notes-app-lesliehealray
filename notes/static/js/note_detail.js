for (const link of document.querySelectorAll('.comment-edit-link')) {
  link.addEventListener('click', event => {
    link.parentElement.querySelector('.note-comment-body').style.display = 'none'
    link.parentElement.querySelector('.comment-edit-form').style.display = 'inline-block'
  })
}

const noteReorderingLink = document.getElementById('note-reordering-link')

let drake

noteReorderingLink.addEventListener('click', (event) => {
  event.preventDefault()
  const noteList = document.getElementById('note-comments')
  console.log('15')

  if (noteReorderingLink.dataset.reordering === 'true') {
    noteList.classList.remove('notelist-reordering')
    drake.destroy()
    noteReorderingLink.classList.remove('button')
    noteReorderingLink.innerText = 'Reorder'
    noteReorderingLink.dataset.reordering = 'false'

    const items = noteList.querySelectorAll('.note-comment')
    const ids = []
    for (const item of items) {
      ids.push(item.dataset.pk)
    }
    fetch(`/notes/${notePk}/reorder/`, {
      method: 'POST',
      body: JSON.stringify(ids)
    }).then(res => res.json()).then(data => console.log(data))
  } else {
    noteList.classList.add('notelist-reordering')
    drake = dragula([noteList])

    noteReorderingLink.classList.add('button')
    noteReorderingLink.innerText = 'Save order'
    noteReorderingLink.dataset.reordering = 'true'
  }
})

