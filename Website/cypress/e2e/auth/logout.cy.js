it('logs out correctly', () => {
  cy.visit('/Logout');
  cy.url().should('include', '/Login');
});