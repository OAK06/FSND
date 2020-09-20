INSERT INTO artists (
    id,
    name,
    genres,
    city,
    state,
    phone,
    website,
    facebook_link,
    seeking_venue,
    seeking_description,
    image_link,
    past_shows_count,
    upcoming_shows_count
) VALUES (
    1,
    'Guns N Petals',
    '["Rock n Roll"]',
    'San Francisco',
    'CA',
    '326-123-5000',
    'https://www.gunsnpetalsband.com',
    'https://www.facebook.com/GunsNPetals',
    True,
    'Looking for shows to perform at in the San Francisco Bay Area!',
    'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80',
    1,
    0
), (
    2,
    'Matt Quevedo',
    '["Jazz"]',
    'New York',
    'NY',
    '300-400-5000',
    NULL,
    'https://www.facebook.com/mattquevedo923251523',
    False,
    NULL,
    'https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80',
    1,
    0
), (
    3,
    'The Wild Sax Band',
    '["Jazz", "Classical"]',
    'San Francisco',
    'CA',
    '432-325-5432',
    NULL,
    NULL,
    False,
    NULL,
    'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
    0,
    3
)
);
INSERT INTO venues(
    id,
    name,
    genres,
    address,
    city,
    state,
    phone,
    website,
    facebook_link,
    seeking_talent,
    seeking_description,
    image_link,
    past_shows_count,
    upcoming_shows_count
) VALUES (
    1,
    'The Musical Hop',
    '["Jazz", "Reggae", "Swing", "Classical", "Folk"]',
    '1015 Folsom Street',
    'San Francisco',
    'CA',
    '123-123-1234',
    'https://www.themusicalhop.com',
    'https://www.facebook.com/TheMusicalHop',
    True,
    'We are on the lookout for a local artist to play every two weeks. Please call us.',
    'https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60',
    1,
    0
), (
    2,
    'The Dueling Pianos Bar',
    '["Classical", "R&B", "Hip-Hop"]',
    '335 Delancey Street',
    'New York',
    'NY',
    '914-003-1132',
    'https://www.theduelingpianos.com',
    'https://www.facebook.com/theduelingpianos',
    False,
    NULL,
    'https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
    0,
    0
), (
    3,
    'Park Square Live Music & Coffee',
    '["Rock n Roll", "Jazz", "Classical", "Folk"]',
    '34 Whiskey Moore Ave',
    'San Francisco',
    'CA',
    '415-000-1234',
    'https://www.parksquarelivemusicandcoffee.com',
    'https://www.facebook.com/ParkSquareLiveMusicAndCoffee',
    False,
    NULL,
    'https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80',
    1,
    1
);
INSERT INTO shows (
    id,
    venue_id,
    artist_id,
    start_time
) VALUES (
    1,
    1,
    1,
    '2019-05-21 21:30:00'
), (
    2,
    3,
    2,
    '2019-06-15 23:00:00'
), (
    3,
    3,
    3,
    '2035-04-01 20:00:00'
);