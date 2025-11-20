function onLoad()
    local notes = self.getGMNotes()
    
    local url = "http://127.0.0.1:9000/character/"
    local headers = {
        ["Content-Type"] = "application/json",
        Accept = "application/json",
    }
        
    local characterData = {
        title = "Character Data",
        body = {notes},
        labels = {"design"}
    }

    local body = JSON.encode(characterData)

    WebSocket.custom(url, "POST", true, body, headers, function(request)
        if request.is_error then
            print("Request failed: " .. request.error)
            return
        end

        print("Status Code:" .. request.response_code)
        local res = JSON.decode(request.text)

        print("Response:" .. res.message)
    end)
end
