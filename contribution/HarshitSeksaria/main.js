// Instance of a div to add a work
let addButton = document.getElementById("addbutton");

// Instance of work list
let list = document.getElementById('workslist');

// Instance of title div
let title = document.getElementById('text');

// Number of works
let works = 0;

// Record of current works
let workTitles = [];

// function to add Typewrite effect
let type = function() {
    setTimeout(() => {
        title.innerHTML += 'T';
    }, 250);

    setTimeout(() => {
        title.innerHTML += 'o';
    }, 500);

    setTimeout(() => {
        title.innerHTML += '-';
    }, 750);

    setTimeout(() => {
        title.innerHTML += 'd';
    }, 1000);

    setTimeout(() => {
        title.innerHTML += 'o';
    }, 1250);

    setTimeout(() => {
        title.innerHTML += ' ';
    }, 1500);

    setTimeout(() => {
        title.innerHTML += 'A';
    }, 1750);

    setTimeout(() => {
        title.innerHTML += 'p';
    }, 2000);

    setTimeout(() => {
        title.innerHTML += 'p';
    }, 2250);

    setTimeout(() => {
        title.innerHTML += 'l';
    }, 2500);

    setTimeout(() => {
        title.innerHTML += 'i';
    }, 2750);

    setTimeout(() => {
        title.innerHTML += 'c';
    }, 3000);

    setTimeout(() => {
        title.innerHTML += 'a';
    }, 3250);

    setTimeout(() => {
        title.innerHTML += 't';
    }, 3500);

    setTimeout(() => {
        title.innerHTML += 'i';
    }, 3750);

    setTimeout(() => {
        title.innerHTML += 'o';
    }, 4000);

    setTimeout(() => {
        title.innerHTML += 'n';
    }, 4250);
}

// Calling type() to start TypeWriter effect.
type();

// Fetch works form localStorage
if (localStorage.getItem('works')) {
    workTitles = localStorage.getItem('works').split(',');
    workTitles.forEach(element => {
        let currentTitle = element;
        let entry = document.createElement('li');

        let div = document.createElement('div');
        div.className = 'works';
        div.id = 'works' + works;
        div.appendChild(document.createTextNode(currentTitle[0].toUpperCase() + currentTitle.slice(1)));
        div.title = 'Click to remove';

        entry.appendChild(div);

        let span = document.createElement('span');
        span.className = 'works remove'
        span.id = 'remove' + works;

        span.onclick = function() {
            let toBeDeleted = document.getElementById('item' + this.id.split('remove')[1]);
            if (workTitles.length != 1)
                workTitles.splice(this.id.split('remove')[1], 1);
            else
                workTitles.pop();
            toBeDeleted.style.transform = 'scale(0)';
            localStorage.setItem('works', workTitles);

            setTimeout(function () {
                list.removeChild(toBeDeleted);
            }, 1000);

            if (workTitles.length == 0) {
                document.getElementsByTagName('h4')[0].innerHTML = 'No Works to do.';
            }
        }

        span.appendChild(document.createTextNode('Done'));

        entry.appendChild(span);
        entry.id = 'item' + works;

        let listitem = list.appendChild(entry);

        listitem.onclick = function() {
            if (workTitles.length != 1)
                workTitles.splice(this.id.split('remove')[1], 1);
            else
                workTitles.pop();
            listitem.style.transform = 'scale(0)'
            localStorage.setItem('works', workTitles);

            setTimeout(() => {
                list.remove(listitem);
            }, 1000);

            if (workTitles.length == 0) {
                document.getElementsByTagName('h4')[0].innerHTML = 'No Works to do.';
            }
        }

        // Show animation when new work get added
        let newWork = document.getElementById('item' + works);
        setTimeout(function () {
            newWork.style.transform = 'scale(1)';
        }, 1);

        works++;
    })
} else {
    document.getElementsByTagName('h4')[0].innerHTML = 'No Works to do.'
}

// ClickListener for addButton
addButton.addEventListener('click', function() {
    let currentTitle = prompt('Add your work here');

    // Check if value is not null
    if (currentTitle) {
        let entry = document.createElement('li');

        let div = document.createElement('div');
        div.className = 'works';
        div.id = 'works' + works;
        div.appendChild(document.createTextNode(currentTitle[0].toUpperCase() + currentTitle.slice(1)));

        entry.appendChild(div);

        let span = document.createElement('span');
        span.className = 'works remove'
        span.id = 'remove' + works;

        span.onclick = function() {
            let toBeDeleted = document.getElementById('item' + this.id.split('remove')[1]);
            if (workTitles.length != 1)
                workTitles.splice(this.id.split('remove')[1], 1);
            else
                workTitles.pop();
            toBeDeleted.style.transform = 'scale(0)';
            localStorage.setItem('works', workTitles);

            setTimeout(function () {
                list.removeChild(toBeDeleted);
            }, 1000);

            if (workTitles.length == 0) 
                document.getElementsByTagName('h4')[0].innerHTML = 'No Works to do.';

        }

        span.appendChild(document.createTextNode('Done'));

        entry.appendChild(span);
        entry.id = 'item' + works;

        let listitem = list.appendChild(entry);

        listitem.onclick = function() {
            if (workTitles.length != 1)
                workTitles.splice(this.id.split('remove')[1], 1);
            else
                workTitles.pop();
            listitem.style.transform = 'scale(0)'
            localStorage.setItem('works', workTitles);

            setTimeout(() => {
                list.remove(listitem);
            }, 1000);

            if (workTitles.length == 0) {
                document.getElementsByTagName('h4')[0].innerHTML = 'No Works to do.';
            }
        }

        // Show animation when work get added
        let newWork = document.getElementById('item' + works);
        setTimeout(function () {
            newWork.style.transform = 'scale(1)';
        }, 1);

        works++;
        workTitles.push(currentTitle);
        document.getElementsByTagName('h4')[0].innerHTML = 'Works to do:'
        localStorage.setItem('works', workTitles);
    }
})