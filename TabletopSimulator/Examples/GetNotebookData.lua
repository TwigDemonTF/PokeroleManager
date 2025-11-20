function getNotebookByTitle(title)
    for _, notebook in pairs(getNotebookTabs()) do
        if notebook.title == title then
            return notebook
        end
    end
    return nil
end

function getNotebookByColor(color)
    for _, notebook in pairs(getNotebookTabs()) do
        if notebook.color == color then
            return notebook
        end
    end
    return nil
end

function onLoad()
    local note = getNotebookByTitle("Data")
    if note then
        printToAll("Found note '" .. note.title .. "': " .. note.body, {1,1,1})
        print(type(note.body))
    else
        printToAll("No note with that title!", {1,0,0})
    end
end
