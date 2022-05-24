from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import info_callback, start_callback

start_info = InlineKeyboardMarkup(row_width=4,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text="Сайт компании⚡",
                                          callback_data=info_callback.new(item_name='site',
                                                                          link='Подробнее')
                                      ),
                                      InlineKeyboardButton(
                                          text="Интернет магазин⭐",
                                          callback_data="info:onlineshop:Подробнее"
                                      )

                                  ], [
                                      InlineKeyboardButton(
                                          text="Одностраничный сайт🌚",
                                          callback_data="info:onepage:Подробнее"
                                      ),
                                      InlineKeyboardButton(
                                          text="Продвижение сайта🌝",
                                          callback_data="info:promote:Подробнее"
                                      )
                                  ], [
                                      InlineKeyboardButton(
                                          text="Контекстная реклама🌎",
                                          callback_data="info:add:Подробнее"
                                      ),
                                      InlineKeyboardButton(
                                          text="Поддержка сайтов🔥",
                                          callback_data="info:supportsite:Подробнее"
                                      )
                                  ], [
                                      InlineKeyboardButton(
                                          text="Создание телеграм ботов🤖",
                                          callback_data="info:develop:Подробнее"
                                      )
                                  ]
                                  ])
siteToBot = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[[
                                     InlineKeyboardButton(
                                         text="Преимущества наших сайтов:",
                                         callback_data="info:advantages:Подробнее"
                                     )
                                 ], [
                                     InlineKeyboardButton(
                                         text="Главное меню",
                                         callback_data="info:menu:Подробнее"
                                     )
                                 ]

                                 ])

sitestart = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[[
                                     InlineKeyboardButton(
                                         text="С чего начать создание сайта компании?:",
                                         callback_data="info:fromstart:Подробнее"
                                     )
                                 ], [
                                     InlineKeyboardButton(
                                         text="Главное меню",
                                         callback_data="info:menu:Подробнее"
                                     )
                                 ]

                                 ])

botInfo = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=[[
                                   InlineKeyboardButton(
                                       text="Основные преимущества ботов:",
                                       callback_data=info_callback.new(item_name='botPluses',
                                                                       link='Подробнее')
                                   )
                               ], [
                                   InlineKeyboardButton(
                                       text="Главное меню",
                                       callback_data="info:menu:Подробнее"
                                   )
                               ]
                               ])

technology = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text="Как же создаются телеграм боты?",
                                          callback_data=info_callback.new(item_name='techno',
                                                                          link='Подробнее')
                                      )
                                  ], [
                                      InlineKeyboardButton(
                                          text="Главное меню",
                                          callback_data="info:menu:Подробнее"
                                      )
                                  ]
                                  ])

examples = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[[
                                    InlineKeyboardButton(
                                        text="Где я могу применить боты?",
                                        callback_data=info_callback.new(item_name='examples',
                                                                        link='Подробнее')
                                    )
                                ], [
                                    InlineKeyboardButton(
                                        text="Главное меню",
                                        callback_data="info:menu:Подробнее"
                                    )
                                ]
                                ])

cost = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[[
                                InlineKeyboardButton(
                                    text="Сколько же это стоит?",
                                    callback_data=info_callback.new(item_name='price',
                                                                    link='Подробнее')
                                )
                            ], [
                                InlineKeyboardButton(
                                    text="Главное меню",
                                    callback_data="info:menu:Подробнее"
                                )
                            ]
                            ])

whyoursite = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text="Почему следует заказать у нас?",
                                          callback_data=info_callback.new(item_name='whyshop',
                                                                          link='Подробнее')
                                      )
                                  ], [
                                      InlineKeyboardButton(
                                          text="Главное меню",
                                          callback_data="info:menu:Подробнее"
                                      )
                                  ]
                                  ])

shopstart = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[[
                                     InlineKeyboardButton(
                                         text="С чего начать создание интернет - магазина?",
                                         callback_data=info_callback.new(item_name='shopstartinfo',
                                                                         link='Подробнее')
                                     )
                                 ], [
                                     InlineKeyboardButton(
                                         text="Главное меню",
                                         callback_data="info:menu:Подробнее"
                                     )
                                 ]
                                 ])

whylanding = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text="Почему следует заказать у нас?",
                                          callback_data=info_callback.new(item_name='whyourlanding',
                                                                          link='Подробнее')
                                      )
                                  ], [
                                      InlineKeyboardButton(
                                          text="Главное меню",
                                          callback_data="info:menu:Подробнее"
                                      )
                                  ]
                                  ])

landingstart = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[[
                                        InlineKeyboardButton(
                                            text="С чего начать создание лендинга?",
                                            callback_data=info_callback.new(item_name='landingstartinfo',
                                                                            link='Подробнее')
                                        )
                                    ], [
                                        InlineKeyboardButton(
                                            text="Главное меню",
                                            callback_data="info:menu:Подробнее"
                                        )
                                    ]
                                    ])

whypromote = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[[
                                      InlineKeyboardButton(
                                          text="Почему следует заказать у нас?",
                                          callback_data=info_callback.new(item_name='whyourpromote',
                                                                          link='Подробнее')
                                      )
                                  ], [
                                      InlineKeyboardButton(
                                          text="Главное меню",
                                          callback_data="info:menu:Подробнее"
                                      )
                                  ]
                                  ])

promotestart = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[[
                                        InlineKeyboardButton(
                                            text="С чего начать сео продвижение сайта?",
                                            callback_data=info_callback.new(item_name='promotestartinfo',
                                                                            link='Подробнее')
                                        )
                                    ], [
                                        InlineKeyboardButton(
                                            text="Главное меню",
                                            callback_data="info:menu:Подробнее"
                                        )
                                    ]
                                    ])

whyadd = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[[
                                  InlineKeyboardButton(
                                      text="Почему следует заказать у нас?",
                                      callback_data=info_callback.new(item_name='whyouradd',
                                                                      link='Подробнее')
                                  )
                              ], [
                                  InlineKeyboardButton(
                                      text="Главное меню",
                                      callback_data="info:menu:Подробнее"
                                  )
                              ]
                              ])

addstart = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[[
                                    InlineKeyboardButton(
                                        text="С чего начать настройку рекламы?",
                                        callback_data=info_callback.new(item_name='addstartinfo',
                                                                        link='Подробнее')
                                    )
                                ], [
                                    InlineKeyboardButton(
                                        text="Главное меню",
                                        callback_data="info:menu:Подробнее"
                                    )
                                ]
                                ])

whysupportsite = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[[
                                  InlineKeyboardButton(
                                      text="Почему следует заказать у нас?",
                                      callback_data=info_callback.new(item_name='whyoursupportsite',
                                                                      link='Подробнее')
                                  )
                              ], [
                                  InlineKeyboardButton(
                                      text="Главное меню",
                                      callback_data="info:menu:Подробнее"
                                  )
                              ]
                              ])

supportsitestart = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[[
                                    InlineKeyboardButton(
                                        text="С чего начать поддержку сайта?",
                                        callback_data=info_callback.new(item_name='supportsitestartinfo',
                                                                        link='Подробнее')
                                    )
                                ], [
                                    InlineKeyboardButton(
                                        text="Главное меню",
                                        callback_data="info:menu:Подробнее"
                                    )
                                ]
                                ])

