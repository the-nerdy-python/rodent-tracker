import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
import RatsList from '../RatsList';

const rats = [
  {
    'active': true,
    'color': 'white',
    'id': 1,
    'weight': 200
  },
  {
    'active': true,
    'color': 'black',
    'id': 2,
    'weight': 300
  }
];

test('RatsList renders properly', () => {
  const wrapper = shallow(<RatsList rats={rats}/>);
  const element = wrapper.find('h4');
  expect(element.length).toBe(2);
  expect(element.get(0).props.children).toBe('white');
});

test('RatsList renders a snapshot properly', () => {
    const tree = renderer.create(<RatsList rats={rats}/>).toJSON();
    expect(tree).toMatchSnapshot();
  });

