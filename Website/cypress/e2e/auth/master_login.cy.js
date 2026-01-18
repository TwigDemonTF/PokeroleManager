it('registers then logs in as a master user', () => {
  const username = `testuser_${Date.now()}`;
  const password = 'TestPassword123';

  // Register first
  cy.visit('/Register');
  cy.get('#username').type(username);
  cy.get('#password').type(password);
  cy.get('button[type="submit"]').click();

  cy.url().should('include', '/Login');

  // Now log in
  cy.get('#username').type(username);
  cy.get('#password').type(password);
  cy.get('button[type="submit"]').click();

  cy.url().should('include', '/Battle');
});
