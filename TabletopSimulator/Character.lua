characterData = {}

function onLoad()
    -- reload saved state
    if self.script_state ~= "" then
        characterData = JSON.decode(self.script_state)
    end
end

function UpdateSelf(params)
    local data = params.data

    characterData = data

    -- Save persistently
    self.script_state = JSON.encode(characterData)

    -- Also expose to other scripts if needed
    self.setVar("characterData", characterData)
end

function GetSelf()
    return characterData
end