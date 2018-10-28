import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';

import AddRat from '../AddRat';

test('AddRat renders properly', () => {
  const wrapper = shallow(<AddRat/>);
  const element = wrapper.find('form');
  expect(element.find('input').length).toBe(3);
  expect(element.find('input').get(0).props.name).toBe('color');
  expect(element.find('input').get(1).props.name).toBe('weight');
  expect(element.find('input').get(2).props.type).toBe('submit');
});

test('AddRat renders a snapshot properly', () => {
  const tree = renderer.create(<AddRat/>).toJSON();
  expect(tree).toMatchSnapshot();
});

