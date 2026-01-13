describe('Player Login (Full Flow)', () => {
  it('creates game data then logs in as player', () => {
    const username = `user_${Date.now()}`;
    const password = 'TestPassword123';
    const playerColor = 'Red';

    // Register user (API)
    cy.request('POST', 'http://127.0.0.1:9000/register', {
      username,
      password
    }).then(res => {
      expect(res.status).to.eq(201);
    });

    // Master login (API) → get gameId
    cy.request('POST', 'http://127.0.0.1:9000/masterLogin', {
      username,
      password
    }).then(loginRes => {
      expect(loginRes.status).to.eq(200);
      const gameId = loginRes.body.gameId;

      // Create BasePokemon (API-only, immutable)
      cy.request('POST', 'http://127.0.0.1:9000/basePokemon', {
        Name: "Test Guy",
        Evolution: null,
        PreEvolution: "Super Test Guy",
        BaseHealth: 5,
        PrimaryType: "STEEL",
        SecondaryType: "GHOST",
        StrengthPotential:  8,
        DexterityPotential: 3,
        VitalityPotential:  4,
        SpecialPotential:   8,
        InsightPotential:   4,
        Strength:  0,
        Dexterity: 0,
        Vitality:  0,
        Special:   0,
        Insight:   0,
        Fight: 0,
        Survival: 0,
        Contest: 0,
        Brawl: 0,
        Channel: 0,
        Clash: 0,
        Evasion: 0,
        Alert: 0,
        Athletic: 0,
        NatureStat: 0,
        Stealth: 0,
        Allure: 0,
        Etiquette: 0,
        Intimidate: 0,
        Perform: 0
      }).then(baseRes => {
        const basePokemonId = baseRes.body.pokemonId;

        // Create GamePokemon with playerColor
        cy.request('POST', 'http://127.0.0.1:9000/gamePokemon', {
          gameId,
          basePokemonId,
          name: 'PlayerMon',
          level: 1,
          gender: 'None',
          age: 0,
          isNpc: false,
          experiencePoints: 0,
          playerColor,
          Guid: crypto.randomUUID(),
          will: 3,
          logic: 1,
          instinct: 1,
          primal: 0,
          garments: []
        });
      });

      // Player login via UI
      cy.visit('/Login');
      cy.get('#username').type(gameId);
      cy.get('#password').type(playerColor.toLowerCase());
      cy.get('input[name="player"]').check();
      cy.get('button[type="submit"]').click();

      cy.url().should('include', '/Player');
    });
  });
});
