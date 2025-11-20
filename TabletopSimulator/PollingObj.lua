local url = "http://127.0.0.1:9000/PullCharacterData/"
local polling = false
local activeCharacters = {}

function onLoad()
    self.addContextMenuItem("Toggle Polling", TogglePolling)
end

-- Main polling loop
function PollLoop()
    if not polling then return end

    for _, guid in ipairs(activeCharacters) do
        print(guid)
        print(url .. guid)
        WebRequest.get(url .. guid, function(request)
            if request.is_error then
                print("Error:", request.error)
            else
                print("Response for", guid, ":", request.text)
                -- Process response here
                local response = JSON.decode(request.text)

                if not response.data then
                    print("Server returned no data. Message:", response.message)
                    return
                end

                local data = response.data

                local obj = getObjectFromGUID(guid)
                if obj then
                    obj.call("UpdateSelf", { data = data })
                end

                print(data.name, data.gender, data.level)
            end
        end)
    end

    -- Repeat every 5 seconds
    Wait.time(PollLoop, 5)
end

function TogglePolling()
    if polling then
        print("Stopping polling.")
        polling = false
    else
        print("Starting polling.")
        activeCharacters = getObjectsWithTag("Pokemon")
        polling = true
        PollLoop()  -- begin loop
    end
end

function getObjectsWithTag(tag)
    local results = {}

    for _, obj in ipairs(getAllObjects()) do
        if obj.hasTag(tag) then
            table.insert(results, obj.getGUID())
        end
    end

    return results
end
