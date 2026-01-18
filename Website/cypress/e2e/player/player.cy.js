describe('Player Page Features', () => {
  let gameId;
  let pokemonGuid;
  let itemId;
  let bagItemId;
  const password = 'TestPassword123';
  const playerColor = 'Red';

//     const loginAsPlayer = (gameId, playerColor) => {
//         cy.visit('/Login');
//         cy.get('#username').type(gameId);
//         cy.get('#password').type(playerColor.toLowerCase());
//         cy.get('input[name="player"]').check();
//         cy.get('button[type="submit"]').click();
//         cy.url().should('include', '/Player');
//     };

//       cy.session(
//         [`player-${gameId}-${playerColor}`],
//         () => {
//         loginAsPlayer(gameId, playerColor);
//         }
//     );

//   // Restore session and go straight to Player page
//   cy.visit('/Player');

  before(() => {
    const username = `user_${Date.now()}`;

    // Register
    cy.request('POST', 'http://127.0.0.1:9090/register', {
      username,
      password
    });

    // Master login
    cy.request('POST', 'http://127.0.0.1:9090/masterLogin', {
      username,
      password
    }).then(res => {
      gameId = res.body.gameId;

      // Create Base Pokémon
      cy.request('POST', 'http://127.0.0.1:9090/basePokemon', {
        Name: "Test Guy",
        Evolution: null,
        PreEvolution: null,
        BaseHealth: 10,
        PrimaryType: "STEEL",
        SecondaryType: "GHOST",
        StrengthPotential: 5,
        DexterityPotential: 5,
        VitalityPotential: 5,
        SpecialPotential: 5,
        InsightPotential: 5,
        Strength: 0,
        Dexterity: 0,
        Vitality: 0,
        Special: 0,
        Insight: 0,
      }).then(baseRes => {
        // Create Game Pokémon
        pokemonGuid = crypto.randomUUID();

        cy.request('POST', 'http://127.0.0.1:9090/gamePokemon', {
          gameId,
          basePokemonId: baseRes.body.pokemonId,
          name: 'PlayerMon',
          level: 1,
          isNpc: false,
          experiencePoints: 100,
          playerColor,
          Guid: pokemonGuid,
          will: 1,
          logic: 0,
          instinct: 0,
          primal: 0,
          garments: []
        });
      });
    });

    // Create equipable + sellable item
    cy.request('POST', 'http://127.0.0.1:9090/Item', {
      name: 'Test Sword',
      description: 'A sword for testing',
      effectKey: 'ATK_UP',
      effectData: { amount: 1 },
      itemCategory: 'Held Item',
      minShopTier: 'Basic Tier',
      isEquipable: true,
      isUsable: false,
      buyPrice: 100,
      sellPrice: 50
    }).then(res => {
      itemId = res.body.id;
    });
  });

  beforeEach(() => {
    cy.visit('/Login');
    cy.get('#username').type(gameId);
    cy.get('#password').type(playerColor.toLowerCase());
    cy.get('input[name="player"]').check();
    cy.get('button[type="submit"]').click();
    cy.url().should('include', '/Player');
  });

  it('renders Pokémon card with name, types, HP, XP, apples', () => {
    cy.contains('PlayerMon').should('exist');
    cy.contains('Steel / Ghost').should('exist');

    cy.contains('Available Experience').should('exist');
    cy.contains('Current Apples').should('exist');

    cy.get('.hp-bar-fill').should('exist');
    cy.get('.lethal-hp-bar-fill').should('exist');
  });

  it('adds item to bag and displays it', () => {
    cy.request(
      'POST',
      `http://127.0.0.1:9090/addItemToBag/${gameId}/${pokemonGuid}/${itemId}`
    );

    cy.reload();

    cy.get('#bagContainer .bag-header').click();
    cy.get('#bagContainer').should('have.class', 'open');

    cy.contains('Test Sword').should('exist');
    cy.contains('Sell for').should('exist');
    cy.contains('Equip').should('exist');
  });

  it('equips an item', () => {
    cy.get('#bagContainer .bag-header').click();

    cy.contains('Equip').click();

    cy.get('.swal2-popup').should('be.visible');
    cy.contains(/equipped/i).should('exist');

    cy.get('#heldItemBadge').should('contain', 'Test Sword');
  });

  it('unequips item via badge', () => {
    cy.get('#heldItemBadge').click();

    cy.get('#heldItemBadge').should('not.exist');
  });

  it('sells an item and gains apples', () => {
    // Open bag
    cy.get('#bagContainer .bag-header').click();
    cy.get('#bagContainer').should('have.class', 'open');

    // Scroll the Sell button into view before clicking
    cy.contains('Sell for')
        .scrollIntoView()
        .should('be.visible')
        .click();

    // Confirm SweetAlert
    cy.get(".swal2-confirm").click()

    // Toast appears
    cy.get('.swal2-popup').should('exist');

    cy.contains('Current Apples: 50').should('exist');
  });

  it('updates HP when backend health changes', () => {
    cy.request('POST', 'http://127.0.0.1:9090/updateHealth', {
      gameId,
      guid: pokemonGuid,
      health: 3
    });

    cy.contains('3 /').should('exist');
  });

  it('sets FAINTED when HP reaches 0', () => {
    cy.request('POST', 'http://127.0.0.1:9090/updateHealth', {
      gameId,
      guid: pokemonGuid,
      health: 0
    });

    cy.contains('Fainted').should('exist');
  });

  it('updates lethal HP bar', () => {
    cy.request('POST', 'http://127.0.0.1:9090/updateLethalHealth', {
      gameId,
      guid: pokemonGuid,
      lethalHealth: 4
    });

    cy.contains('4 /').should('exist');
  });

  it('adds XP and updates UI', () => {
    cy.request('POST', `http://127.0.0.1:9090/addXp/${gameId}/${pokemonGuid}`, {
      xp: 25
    });

    cy.contains('Available Experience').should('contain', '125');
  });

  it('buys a stat (Strength)', () => {
    cy.contains('Strength').click();

    cy.contains('Increase Strength?').should('exist');
    cy.contains('Buy').click();

    cy.contains('Strength increased!').should('exist');
  });

  it('toggles bag open/close', () => {
    cy.get('#bagContainer').as('bag');

    cy.get('@bag').should('not.have.class', 'open');
    cy.get('@bag').find('.bag-header').click();
    cy.get('@bag').should('have.class', 'open');
  });

  it('adds item to bag via API and displays it', () => {
    // assumes item with ID 1 exists
    cy.request('POST', `http://127.0.0.1:9090/addItemToBag/${gameId}/${pokemonGuid}/1`);

    cy.reload();
    cy.contains('Sell for').should('exist');
  });
});
