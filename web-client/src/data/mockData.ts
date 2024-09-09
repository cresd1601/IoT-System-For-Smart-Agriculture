import { tokens } from '@/styles/theme'

export const mockDataTeam = [
  {
    id: 1,
    name: 'Jon Snow',
    email: 'jonsnow@gmail.com',
    age: 35,
    phone: '(665)121-5454',
    access: 'admin',
  },
  {
    id: 2,
    name: 'Cersei Lannister',
    email: 'cerseilannister@gmail.com',
    age: 42,
    phone: '(421)314-2288',
    access: 'manager',
  },
  {
    id: 3,
    name: 'Jaime Lannister',
    email: 'jaimelannister@gmail.com',
    age: 45,
    phone: '(422)982-6739',
    access: 'user',
  },
  {
    id: 4,
    name: 'Anya Stark',
    email: 'anyastark@gmail.com',
    age: 16,
    phone: '(921)425-6742',
    access: 'admin',
  },
  {
    id: 5,
    name: 'Daenerys Targaryen',
    email: 'daenerystargaryen@gmail.com',
    age: 31,
    phone: '(421)445-1189',
    access: 'user',
  },
  {
    id: 6,
    name: 'Ever Melisandre',
    email: 'evermelisandre@gmail.com',
    age: 150,
    phone: '(232)545-6483',
    access: 'manager',
  },
  {
    id: 7,
    name: 'Ferrara Clifford',
    email: 'ferraraclifford@gmail.com',
    age: 44,
    phone: '(543)124-0123',
    access: 'user',
  },
  {
    id: 8,
    name: 'Rossini Frances',
    email: 'rossinifrances@gmail.com',
    age: 36,
    phone: '(222)444-5555',
    access: 'user',
  },
  {
    id: 9,
    name: 'Harvey Roxie',
    email: 'harveyroxie@gmail.com',
    age: 65,
    phone: '(444)555-6239',
    access: 'admin',
  },
]

export const mockDataInvoices = [
  {
    id: 1,
    name: 'Jon Snow',
    email: 'jonsnow@gmail.com',
    cost: '21.24',
    phone: '(665)121-5454',
    date: '03/12/2022',
  },
  {
    id: 2,
    name: 'Cersei Lannister',
    email: 'cerseilannister@gmail.com',
    cost: '1.24',
    phone: '(421)314-2288',
    date: '06/15/2021',
  },
  {
    id: 3,
    name: 'Jaime Lannister',
    email: 'jaimelannister@gmail.com',
    cost: '11.24',
    phone: '(422)982-6739',
    date: '05/02/2022',
  },
  {
    id: 4,
    name: 'Anya Stark',
    email: 'anyastark@gmail.com',
    cost: '80.55',
    phone: '(921)425-6742',
    date: '03/21/2022',
  },
  {
    id: 5,
    name: 'Daenerys Targaryen',
    email: 'daenerystargaryen@gmail.com',
    cost: '1.24',
    phone: '(421)445-1189',
    date: '01/12/2021',
  },
  {
    id: 6,
    name: 'Ever Melisandre',
    email: 'evermelisandre@gmail.com',
    cost: '63.12',
    phone: '(232)545-6483',
    date: '11/02/2022',
  },
  {
    id: 7,
    name: 'Ferrara Clifford',
    email: 'ferraraclifford@gmail.com',
    cost: '52.42',
    phone: '(543)124-0123',
    date: '02/11/2022',
  },
  {
    id: 8,
    name: 'Rossini Frances',
    email: 'rossinifrances@gmail.com',
    cost: '21.24',
    phone: '(222)444-5555',
    date: '05/02/2021',
  },
]

export const mockTransactions = [
  {
    txId: '01e4dsa',
    user: 'johndoe',
    date: '2021-09-01',
    cost: '43.95',
  },
  {
    txId: '0315dsaa',
    user: 'jackdower',
    date: '2022-04-01',
    cost: '133.45',
  },
  {
    txId: '01e4dsa',
    user: 'aberdohnny',
    date: '2021-09-01',
    cost: '43.95',
  },
  {
    txId: '51034szv',
    user: 'goodmanave',
    date: '2022-11-05',
    cost: '200.95',
  },
  {
    txId: '0a123sb',
    user: 'stevebower',
    date: '2022-11-02',
    cost: '13.55',
  },
  {
    txId: '01e4dsa',
    user: 'aberdohnny',
    date: '2021-09-01',
    cost: '43.95',
  },
  {
    txId: '120s51a',
    user: 'wootzifer',
    date: '2019-04-15',
    cost: '24.20',
  },
  {
    txId: '0315dsaa',
    user: 'jackdower',
    date: '2022-04-01',
    cost: '133.45',
  },
]

export const mockBarData = [
  {
    country: 'US',
    donut: 140,
    donutColor: 'hsl(340, 70%, 50%)',
  },
  {
    country: 'JP',
    donut: 29,
    donutColor: 'hsl(275, 70%, 50%)',
  },
  {
    country: 'RU',
    donut: 152,
    donutColor: 'hsl(256, 70%, 50%)',
  },
  {
    country: 'CN',
    donut: 83,
    donutColor: 'hsl(9, 70%, 50%)',
  },
  {
    country: 'BR',
    donut: 35,
    donutColor: 'hsl(285, 70%, 50%)',
  },
  {
    country: 'NZ',
    donut: 18,
    donutColor: 'hsl(76, 70%, 50%)',
  },
  {
    country: 'IN',
    donut: 49,
    donutColor: 'hsl(274, 70%, 50%)',
  },
]

export const mockPieData = [
  {
    id: 'ruby',
    label: 'ruby',
    value: 239,
    color: 'hsl(104, 70%, 50%)',
  },
  {
    id: 'go',
    label: 'go',
    value: 170,
    color: 'hsl(162, 70%, 50%)',
  },
  {
    id: 'php',
    label: 'php',
    value: 322,
    color: 'hsl(291, 70%, 50%)',
  },
  {
    id: 'python',
    label: 'python',
    value: 503,
    color: 'hsl(229, 70%, 50%)',
  },
  {
    id: 'javascript',
    label: 'javascript',
    value: 584,
    color: 'hsl(344, 70%, 50%)',
  },
]

export const mockLineData = [
  {
    id: 'Minimum',
    color: tokens('dark').blueAccent[500],
    data: [
      {
        x: '00:00',
        y: 5,
      },
      {
        x: '01:00',
        y: 5,
      },
      {
        x: '02:00',
        y: 5,
      },
      {
        x: '03:00',
        y: 5,
      },
      {
        x: '04:00',
        y: 5,
      },
      {
        x: '05:00',
        y: 5,
      },
      {
        x: '06:00',
        y: 5,
      },
      {
        x: '07:00',
        y: 5,
      },
      {
        x: '08:00',
        y: 5,
      },
      {
        x: '09:00',
        y: 5,
      },
      {
        x: '10:00',
        y: 5,
      },
      {
        x: '11:00',
        y: 5,
      },
      {
        x: '12:00',
        y: 5,
      },
    ],
  },
  {
    id: 'Temperatures',
    color: tokens('dark').greenAccent[600],
    data: [
      {
        x: '00:00',
        y: 29,
      },
      {
        x: '01:00',
        y: 29,
      },
      {
        x: '02:00',
        y: 28,
      },
      {
        x: '03:00',
        y: 27,
      },
      {
        x: '04:00',
        y: 27,
      },
      {
        x: '05:00',
        y: 26,
      },
      {
        x: '06:00',
        y: 26,
      },
      {
        x: '07:00',
        y: 25,
      },
      {
        x: '08:00',
        y: 25,
      },
      {
        x: '09:00',
        y: 26,
      },
      {
        x: '10:00',
        y: 28,
      },
      {
        x: '11:00',
        y: 30,
      },
      {
        x: '12:00',
        y: 32,
      },
    ],
  },
  {
    id: 'Maximum',
    color: tokens('dark').redAccent[500],
    data: [
      {
        x: '00:00',
        y: 35,
      },
      {
        x: '01:00',
        y: 35,
      },
      {
        x: '02:00',
        y: 35,
      },
      {
        x: '03:00',
        y: 35,
      },
      {
        x: '04:00',
        y: 35,
      },
      {
        x: '05:00',
        y: 35,
      },
      {
        x: '06:00',
        y: 35,
      },
      {
        x: '07:00',
        y: 35,
      },
      {
        x: '08:00',
        y: 35,
      },
      {
        x: '09:00',
        y: 35,
      },
      {
        x: '10:00',
        y: 35,
      },
      {
        x: '11:00',
        y: 35,
      },
      {
        x: '12:00',
        y: 35,
      },
    ],
  },
]

export const mockHumidityData = [
  {
    id: 'Minimum',
    color: tokens('dark').blueAccent[500],
    data: [
      {
        x: '00:00',
        y: 50,
      },
      {
        x: '01:00',
        y: 50,
      },
      {
        x: '02:00',
        y: 50,
      },
      {
        x: '03:00',
        y: 50,
      },
      {
        x: '04:00',
        y: 50,
      },
      {
        x: '05:00',
        y: 50,
      },
      {
        x: '06:00',
        y: 50,
      },
      {
        x: '07:00',
        y: 50,
      },
      {
        x: '08:00',
        y: 50,
      },
      {
        x: '09:00',
        y: 50,
      },
      {
        x: '10:00',
        y: 50,
      },
      {
        x: '11:00',
        y: 50,
      },
      {
        x: '12:00',
        y: 50,
      },
    ],
  },
  {
    id: 'Humidity',
    color: tokens('dark').greenAccent[300],
    data: [
      {
        x: '00:00',
        y: 81,
      },
      {
        x: '01:00',
        y: 62,
      },
      {
        x: '02:00',
        y: 63,
      },
      {
        x: '03:00',
        y: 63,
      },
      {
        x: '04:00',
        y: 66,
      },
      {
        x: '05:00',
        y: 68,
      },
      {
        x: '06:00',
        y: 70,
      },
      {
        x: '07:00',
        y: 69,
      },
      {
        x: '08:00',
        y: 72,
      },
      {
        x: '09:00',
        y: 76,
      },
      {
        x: '10:00',
        y: 76,
      },
      {
        x: '11:00',
        y: 74,
      },
      {
        x: '12:00',
        y: 67,
      },
    ],
  },
  {
    id: 'Maximum',
    color: tokens('dark').redAccent[500],
    data: [
      {
        x: '00:00',
        y: 100,
      },
      {
        x: '01:00',
        y: 100,
      },
      {
        x: '02:00',
        y: 100,
      },
      {
        x: '03:00',
        y: 100,
      },
      {
        x: '04:00',
        y: 100,
      },
      {
        x: '05:00',
        y: 100,
      },
      {
        x: '06:00',
        y: 100,
      },
      {
        x: '07:00',
        y: 100,
      },
      {
        x: '08:00',
        y: 100,
      },
      {
        x: '09:00',
        y: 100,
      },
      {
        x: '10:00',
        y: 100,
      },
      {
        x: '11:00',
        y: 100,
      },
      {
        x: '12:00',
        y: 100,
      },
    ],
  },
]

export const mockMoistureData = [
  {
    id: 'Minimum',
    color: tokens('dark').blueAccent[500],
    data: [
      {
        x: '00:00',
        y: 50,
      },
      {
        x: '01:00',
        y: 50,
      },
      {
        x: '02:00',
        y: 50,
      },
      {
        x: '03:00',
        y: 50,
      },
      {
        x: '04:00',
        y: 50,
      },
      {
        x: '05:00',
        y: 50,
      },
      {
        x: '06:00',
        y: 50,
      },
      {
        x: '07:00',
        y: 50,
      },
      {
        x: '08:00',
        y: 50,
      },
      {
        x: '09:00',
        y: 50,
      },
      {
        x: '10:00',
        y: 50,
      },
      {
        x: '11:00',
        y: 50,
      },
      {
        x: '12:00',
        y: 50,
      },
    ],
  },
  {
    id: 'Moisture',
    color: tokens('dark').grey[300],
    data: [
      {
        x: '00:00',
        y: 45,
      },
      {
        x: '01:00',
        y: 55,
      },
      {
        x: '02:00',
        y: 54,
      },
      {
        x: '03:00',
        y: 54,
      },
      {
        x: '04:00',
        y: 52,
      },
      {
        x: '05:00',
        y: 52,
      },
      {
        x: '06:00',
        y: 51,
      },
      {
        x: '07:00',
        y: 50,
      },
      {
        x: '08:00',
        y: 48,
      },
      {
        x: '09:00',
        y: 51,
      },
      {
        x: '10:00',
        y: 55,
      },
      {
        x: '11:00',
        y: 60,
      },
      {
        x: '12:00',
        y: 58,
      },
    ],
  },
  {
    id: 'Maximum',
    color: tokens('dark').redAccent[500],
    data: [
      {
        x: '00:00',
        y: 100,
      },
      {
        x: '01:00',
        y: 100,
      },
      {
        x: '02:00',
        y: 100,
      },
      {
        x: '03:00',
        y: 100,
      },
      {
        x: '04:00',
        y: 100,
      },
      {
        x: '05:00',
        y: 100,
      },
      {
        x: '06:00',
        y: 100,
      },
      {
        x: '07:00',
        y: 100,
      },
      {
        x: '08:00',
        y: 100,
      },
      {
        x: '09:00',
        y: 100,
      },
      {
        x: '10:00',
        y: 100,
      },
      {
        x: '11:00',
        y: 100,
      },
      {
        x: '12:00',
        y: 100,
      },
    ],
  },
]

export const mockGeographyData = [
  {
    id: 'AFG',
    value: 520600,
  },
  {
    id: 'AGO',
    value: 949905,
  },
  {
    id: 'ALB',
    value: 329910,
  },
  {
    id: 'ARE',
    value: 675484,
  },
  {
    id: 'ARG',
    value: 432239,
  },
  {
    id: 'ARM',
    value: 288305,
  },
  {
    id: 'ATA',
    value: 415648,
  },
  {
    id: 'ATF',
    value: 665159,
  },
  {
    id: 'AUT',
    value: 798526,
  },
  {
    id: 'AZE',
    value: 481678,
  },
  {
    id: 'BDI',
    value: 496457,
  },
  {
    id: 'BEL',
    value: 252276,
  },
  {
    id: 'BEN',
    value: 440315,
  },
  {
    id: 'BFA',
    value: 343752,
  },
  {
    id: 'BGD',
    value: 920203,
  },
  {
    id: 'BGR',
    value: 261196,
  },
  {
    id: 'BHS',
    value: 421551,
  },
  {
    id: 'BIH',
    value: 974745,
  },
  {
    id: 'BLR',
    value: 349288,
  },
  {
    id: 'BLZ',
    value: 305983,
  },
  {
    id: 'BOL',
    value: 430840,
  },
  {
    id: 'BRN',
    value: 345666,
  },
  {
    id: 'BTN',
    value: 649678,
  },
  {
    id: 'BWA',
    value: 319392,
  },
  {
    id: 'CAF',
    value: 722549,
  },
  {
    id: 'CAN',
    value: 332843,
  },
  {
    id: 'CHE',
    value: 122159,
  },
  {
    id: 'CHL',
    value: 811736,
  },
  {
    id: 'CHN',
    value: 593604,
  },
  {
    id: 'CIV',
    value: 143219,
  },
  {
    id: 'CMR',
    value: 630627,
  },
  {
    id: 'COG',
    value: 498556,
  },
  {
    id: 'COL',
    value: 660527,
  },
  {
    id: 'CRI',
    value: 60262,
  },
  {
    id: 'CUB',
    value: 177870,
  },
  {
    id: '-99',
    value: 463208,
  },
  {
    id: 'CYP',
    value: 945909,
  },
  {
    id: 'CZE',
    value: 500109,
  },
  {
    id: 'DEU',
    value: 63345,
  },
  {
    id: 'DJI',
    value: 634523,
  },
  {
    id: 'DNK',
    value: 731068,
  },
  {
    id: 'DOM',
    value: 262538,
  },
  {
    id: 'DZA',
    value: 760695,
  },
  {
    id: 'ECU',
    value: 301263,
  },
  {
    id: 'EGY',
    value: 148475,
  },
  {
    id: 'ERI',
    value: 939504,
  },
  {
    id: 'ESP',
    value: 706050,
  },
  {
    id: 'EST',
    value: 977015,
  },
  {
    id: 'ETH',
    value: 461734,
  },
  {
    id: 'FIN',
    value: 22800,
  },
  {
    id: 'FJI',
    value: 18985,
  },
  {
    id: 'FLK',
    value: 64986,
  },
  {
    id: 'FRA',
    value: 447457,
  },
  {
    id: 'GAB',
    value: 669675,
  },
  {
    id: 'GBR',
    value: 757120,
  },
  {
    id: 'GEO',
    value: 158702,
  },
  {
    id: 'GHA',
    value: 893180,
  },
  {
    id: 'GIN',
    value: 877288,
  },
  {
    id: 'GMB',
    value: 724530,
  },
  {
    id: 'GNB',
    value: 387753,
  },
  {
    id: 'GNQ',
    value: 706118,
  },
  {
    id: 'GRC',
    value: 377796,
  },
  {
    id: 'GTM',
    value: 66890,
  },
  {
    id: 'GUY',
    value: 719300,
  },
  {
    id: 'HND',
    value: 739590,
  },
  {
    id: 'HRV',
    value: 929467,
  },
  {
    id: 'HTI',
    value: 538961,
  },
  {
    id: 'HUN',
    value: 146095,
  },
  {
    id: 'IDN',
    value: 490681,
  },
  {
    id: 'IND',
    value: 549818,
  },
  {
    id: 'IRL',
    value: 630163,
  },
  {
    id: 'IRN',
    value: 596921,
  },
  {
    id: 'IRQ',
    value: 767023,
  },
  {
    id: 'ISL',
    value: 478682,
  },
  {
    id: 'ISR',
    value: 963688,
  },
  {
    id: 'ITA',
    value: 393089,
  },
  {
    id: 'JAM',
    value: 83173,
  },
  {
    id: 'JOR',
    value: 52005,
  },
  {
    id: 'JPN',
    value: 199174,
  },
  {
    id: 'KAZ',
    value: 181424,
  },
  {
    id: 'KEN',
    value: 60946,
  },
  {
    id: 'KGZ',
    value: 432478,
  },
  {
    id: 'KHM',
    value: 254461,
  },
  {
    id: 'OSA',
    value: 942447,
  },
  {
    id: 'KWT',
    value: 414413,
  },
  {
    id: 'LAO',
    value: 448339,
  },
  {
    id: 'LBN',
    value: 620090,
  },
  {
    id: 'LBR',
    value: 435950,
  },
  {
    id: 'LBY',
    value: 75091,
  },
  {
    id: 'LKA',
    value: 595124,
  },
  {
    id: 'LSO',
    value: 483524,
  },
  {
    id: 'LTU',
    value: 867357,
  },
  {
    id: 'LUX',
    value: 689172,
  },
  {
    id: 'LVA',
    value: 742980,
  },
  {
    id: 'MAR',
    value: 236538,
  },
  {
    id: 'MDA',
    value: 926836,
  },
  {
    id: 'MDG',
    value: 840840,
  },
  {
    id: 'MEX',
    value: 353910,
  },
  {
    id: 'MKD',
    value: 505842,
  },
  {
    id: 'MLI',
    value: 286082,
  },
  {
    id: 'MMR',
    value: 915544,
  },
  {
    id: 'MNE',
    value: 609500,
  },
  {
    id: 'MNG',
    value: 410428,
  },
  {
    id: 'MOZ',
    value: 32868,
  },
  {
    id: 'MRT',
    value: 375671,
  },
  {
    id: 'MWI',
    value: 591935,
  },
  {
    id: 'MYS',
    value: 991644,
  },
  {
    id: 'NAM',
    value: 701897,
  },
  {
    id: 'NCL',
    value: 144098,
  },
  {
    id: 'NER',
    value: 312944,
  },
  {
    id: 'NGA',
    value: 862877,
  },
  {
    id: 'NIC',
    value: 90831,
  },
  {
    id: 'NLD',
    value: 281879,
  },
  {
    id: 'NOR',
    value: 224537,
  },
  {
    id: 'NPL',
    value: 322331,
  },
  {
    id: 'NZL',
    value: 86615,
  },
  {
    id: 'OMN',
    value: 707881,
  },
  {
    id: 'PAK',
    value: 158577,
  },
  {
    id: 'PAN',
    value: 738579,
  },
  {
    id: 'PER',
    value: 248751,
  },
  {
    id: 'PHL',
    value: 557292,
  },
  {
    id: 'PNG',
    value: 516874,
  },
  {
    id: 'POL',
    value: 682137,
  },
  {
    id: 'PRI',
    value: 957399,
  },
  {
    id: 'PRT',
    value: 846430,
  },
  {
    id: 'PRY',
    value: 720555,
  },
  {
    id: 'QAT',
    value: 478726,
  },
  {
    id: 'ROU',
    value: 259318,
  },
  {
    id: 'RUS',
    value: 268735,
  },
  {
    id: 'RWA',
    value: 136781,
  },
  {
    id: 'ESH',
    value: 151957,
  },
  {
    id: 'SAU',
    value: 111821,
  },
  {
    id: 'SDN',
    value: 927112,
  },
  {
    id: 'SDS',
    value: 966473,
  },
  {
    id: 'SEN',
    value: 158085,
  },
  {
    id: 'SLB',
    value: 178389,
  },
  {
    id: 'SLE',
    value: 528433,
  },
  {
    id: 'SLV',
    value: 353467,
  },
  {
    id: 'ABV',
    value: 251,
  },
  {
    id: 'SOM',
    value: 445243,
  },
  {
    id: 'SRB',
    value: 202402,
  },
  {
    id: 'SUR',
    value: 972121,
  },
  {
    id: 'SVK',
    value: 319923,
  },
  {
    id: 'SVN',
    value: 728766,
  },
  {
    id: 'SWZ',
    value: 379669,
  },
  {
    id: 'SYR',
    value: 16221,
  },
  {
    id: 'TCD',
    value: 101273,
  },
  {
    id: 'TGO',
    value: 498411,
  },
  {
    id: 'THA',
    value: 506906,
  },
  {
    id: 'TJK',
    value: 613093,
  },
  {
    id: 'TKM',
    value: 327016,
  },
  {
    id: 'TLS',
    value: 607972,
  },
  {
    id: 'TTO',
    value: 936365,
  },
  {
    id: 'TUN',
    value: 898416,
  },
  {
    id: 'TUR',
    value: 237783,
  },
  {
    id: 'TWN',
    value: 878213,
  },
  {
    id: 'TZA',
    value: 442174,
  },
  {
    id: 'UGA',
    value: 720710,
  },
  {
    id: 'UKR',
    value: 74172,
  },
  {
    id: 'URY',
    value: 753177,
  },
  {
    id: 'USA',
    value: 658725,
  },
  {
    id: 'UZB',
    value: 550313,
  },
  {
    id: 'VEN',
    value: 707492,
  },
  {
    id: 'VNM',
    value: 538907,
  },
  {
    id: 'VUT',
    value: 650646,
  },
  {
    id: 'PSE',
    value: 476078,
  },
  {
    id: 'YEM',
    value: 957751,
  },
  {
    id: 'ZAF',
    value: 836949,
  },
  {
    id: 'ZMB',
    value: 714503,
  },
  {
    id: 'ZWE',
    value: 405217,
  },
  {
    id: 'KOR',
    value: 171135,
  },
]
